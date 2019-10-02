import job
from abaqus import *
from abaqusConstants import *


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


model = mdb.models['axial-mesh']
applyMaterialProperties(mat)
func = '2*%(P0)f*%(delta)f*%(k)f/pi/%(a)f**2/(1-exp(-2*%(r0)f**2/%(a)f**2))*exp(-2*X**2/%(a)f**2)*exp(-%(k)f*Y)'\
    % pars
model.ExpressionField(name='HG', localCsys=None,
                      description='',
                      expression=func)
jb = mdb.jobs['axial_mesh']
jb.submit(consistencyChecking=OFF)
jb.waitForCompletion()

import odbAccess
odb = session.openOdb(name='axial_mesh.odb')
odb = session.odbs.values()[0]
fot = odb.steps.values()[-1].frames[-1].fieldOutputs['NT11']
fou = odb.steps.values()[-1].frames[-1].fieldOutputs['U']
inst = odb.rootAssembly.instances.values()[0]
fname = '%s_out_P0=%3.1f_a=%4.2f.txt' % (
    mat_name, pars['P0'], pars['a'] * 1000)
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
