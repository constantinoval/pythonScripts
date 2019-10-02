from odbAccess import *
from abaqusConstants import *
from math import sqrt

def calcF(odb, instance, setName, crit, frame=-1, fname='reportF.txt'):
    fl=open(fname, 'w')
    ss=odb.rootAssembly.instances[instance].elementSets
    fo=odb.steps.values()[0].frames[frame].fieldOutputs['S']
    es=ss[setName]
    sp=es.elements[0].sectionCategory.sectionPoints
    fo1=fo.getSubset(region=es)
    maxF=-1e9
    maxFply=-1
    for i, p in enumerate(sp):
        m=crit(i)
        p1=fo1.getSubset(sectionPoint=p)
        ss11=p1.getScalarField(componentLabel='S11')
        ss22=p1.getScalarField(componentLabel='S22')
        ss12=p1.getScalarField(componentLabel='S12')
        mx=-1e20
        for s1v, s2v, s12v in zip(ss11.values, ss22.values, ss12.values):
            s1=s1v.data
            s2=s2v.data
            s12=s12v.data
            f=m['F1']*s1+m['F2']*s2+m['F11']*s1**2\
              +m['F22']*s2**2+m['F33']*s12**2\
              +2*m['F12']*s1*s2
            mx=max(mx, f)
        print 'ply ', i+1, ': fmax=', mx
        fl.write('ply {0}: Ifmax={1}\n'.format(i+1, mx))
        if mx>maxF:
            maxF=mx
            maxFply=i+1
    fl.write('maxF={}, in ply {}'.format(maxF, maxFply))
    fl.close()
    print 'maxF={}, in ply {}'.format(maxF, maxFply)
    return maxFply

def createField(odb, instance, setName, crit, ply=0, frame=-1, name='F'):
    ss=odb.rootAssembly.instances[instance].elementSets
    fo=odb.steps.values()[0].frames[frame].fieldOutputs['S']
    if odb.steps.has_key('Session Step'):
        sessionStep=odb.steps['Session Step']
    else:
        sessionStep = odb.Step(name='Session Step',
            description='Step for Viewer non-persistent fields', domain=TIME,
            timePeriod=1.0)
    if len(sessionStep.frames):
        sessionFrame=sessionStep.frames[0]
    else:
        sessionFrame = sessionStep.Frame(frameId=0, frameValue=0.0,
            description='Session Frame')

    es=ss[setName]
    sp=es.elements[0].sectionCategory.sectionPoints
    fo1=fo.getSubset(region=es)
    p=sp[ply-1]
    m=crit(ply-1)
    p1=fo1.getSubset(sectionPoint=p)
    s11=p1.getScalarField(componentLabel='S11')
    s22=p1.getScalarField(componentLabel='S22')
    s12=p1.getScalarField(componentLabel='S12')
    tmpfield=m['F1']*s11+m['F2']*s22+m['F11']*s11*s11+m['F22']*s22*s22\
             +m['F33']*s12*s12+2*m['F12']*s11*s22
    sessionField = sessionFrame.FieldOutput(name=name,
    description='', field=tmpfield)