import job
import os
import json
from abaqus import *
from abaqusConstants import *

PP = [0.5]#, 0.7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aa = [0.7]#, 0.5, 0.1, 0.05]


model = mdb.models['axial-mesh']


def applyMaterialProperties(mat):
    model.materials['Material-1'].conductivity.setValues(
        table=((mat['conductivity'], ), ))
    model.materials['Material-1'].density.setValues(table=((mat['rho'],), ))
    model.materials['Material-1'].elastic.setValues(
        table=((mat['E'], mat['nu']), ))
    model.materials['Material-1'].expansion.setValues(
        type=ISOTROPIC, table=((mat['alpha'], ), ))
    model.materials['Material-1'].specificHeat.setValues(
        table=((mat['Cp'], ), ))


materials = json.load(open('materials.json', 'r'))
r0 = 6.25e-3
for mat_name, mat in materials.iteritems():
    applyMaterialProperties(mat)
    print 'Crystal:', mat_name
    for P0 in PP:
        for a in aa:
            if os.path.exists('%s_out_P0=%3.1f_a=%4.2f.txt' % (mat_name, P0, a)):
                print 'Sciping file ', '%s_out_P0=%3.1f_a=%4.2f.txt' % (mat_name, P0, a), ' because exists'
                continue
            pars = {'a': a * 1e-3, 'P0': P0,
                    'k': mat['k'], 'delta': mat['delta'], 'r0': r0}
            print 'Creating load...'
            print 'P0=', P0, 'W', 'a=', a, 'mm'
            func = '2*%(P0)f*%(delta)f*%(k)f/pi/%(a)f**2/(1-exp(-2*%(r0)f**2/%(a)f**2))*exp(-2*X**2/%(a)f**2)*exp(-%(k)f*Y)'\
                % pars
            # print func
            model.ExpressionField(name='HG', localCsys=None,
                                  description='',
                                  expression=func)
            print 'Submitting...'
            jb = mdb.jobs['axial_mesh']
            jb.submit(consistencyChecking=OFF)
            jb.waitForCompletion()

            print 'Solution done...'
            print 'Postprocessing...'

            import odbAccess
            odb = session.openOdb(name='axial_mesh.odb')
            odb = session.odbs.values()[0]
            fot = odb.steps.values()[-1].frames[-1].fieldOutputs['NT11']
            fou = odb.steps.values()[-1].frames[-1].fieldOutputs['U']
            inst = odb.rootAssembly.instances.values()[0]
            fname = '%s_out_P0=%3.1f_a=%4.2f.txt' % (mat_name, P0, a)
            print 'Writing result to file', fname
            f = open(fname, 'w')
            f.write('Label, coordinates, T, U\n')
            for fvt, fvu in zip(fot.values, fou.values):
                nl = fvt.nodeLabel
                n1 = inst.getNodeFromLabel(nl)
                crds = n1.coordinates
                temp = fvt.data
                u = fvu.data
                fmt = ', '.join(['%d'] + ['%e'] *
                                (len(crds) + 1 + len(u))) + '\n'
                f.write(fmt % tuple([nl] + list(crds) + [temp] + u.tolist()))
                del n1
            f.close()
