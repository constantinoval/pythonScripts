from odbAccess import *
from calcF import calcF, createField
from math import sqrt
from collections import defaultdict

#
instance='BOCHKA_FULL-1'
frame=-1
#
#-----------
K=1
#-----------
roving=dict()
roving['s1p']=146.7e6/K
roving['s1m']=67.0e6/K
roving['s2p']=3.8e6/K
roving['s2m']=18.9e6/K
roving['s12']=9.0e6/K
roving['s12p']=roving['s12m']=roving['s12']

rovingF=dict()
rovingF['F1']=1.0/roving['s1p']-1.0/roving['s1m']
rovingF['F2']=1.0/roving['s2p']-1.0/roving['s2m']
rovingF['F11']=1.0/roving['s1p']/roving['s1m']
rovingF['F22']=1.0/roving['s2p']/roving['s2m']
rovingF['F33']=1.0/roving['s12']**2
rovingF['F12']=-0.5*sqrt(rovingF['F11']*rovingF['F22'])

for k in rovingF.keys():
    exec(k+'='+str(rovingF[k]))

rovingF.update(roving)

steklotk1=dict()
steklotk1['s1p']=39.3e6/K
steklotk1['s1m']=41.6e6/K
steklotk1['s2p']=39.3e6/K
steklotk1['s2m']=41.6e6/K
steklotk1['s12']=30.9e6/K
steklotk1['s12p']=steklotk1['s12m']=steklotk1['s12']

steklotk1F=dict()
steklotk1F['F1']=1.0/steklotk1['s1p']-1.0/steklotk1['s1m']
steklotk1F['F2']=1.0/steklotk1['s2p']-1.0/steklotk1['s2m']
steklotk1F['F11']=1.0/steklotk1['s1p']/steklotk1['s1m']
steklotk1F['F22']=1.0/steklotk1['s2p']/steklotk1['s2m']
steklotk1F['F33']=1.0/steklotk1['s12']**2
steklotk1F['F12']=-0.5*sqrt(steklotk1F['F11']*steklotk1F['F22'])

for k in steklotk1F.keys():
    exec(k+'='+str(steklotk1F[k]))

steklotk1F.update(steklotk1)

steklotk2=dict()
steklotk2['s1p']=53.7e6/K
steklotk2['s1m']=47.7e6/K
steklotk2['s2p']=53.7e6/K
steklotk2['s2m']=47.7e6/K
steklotk2['s12']=39.5e6/K
steklotk2['s12p']=steklotk1['s12m']=steklotk1['s12']

steklotk2F=dict()
steklotk2F['F1']=1.0/steklotk2['s1p']-1.0/steklotk2['s1m']
steklotk2F['F2']=1.0/steklotk2['s2p']-1.0/steklotk2['s2m']
steklotk2F['F11']=1.0/steklotk2['s1p']/steklotk2['s1m']
steklotk2F['F22']=1.0/steklotk2['s2p']/steklotk2['s2m']
steklotk2F['F33']=1.0/steklotk2['s12']**2
steklotk2F['F12']=-0.5*sqrt(steklotk2F['F11']*steklotk2F['F22'])

for k in steklotk2F.keys():
    exec(k+'='+str(steklotk2F[k]))

steklotk2F.update(steklotk2)


#------------------------------
odb=session.odbs.values()[-1]

print 'Calculating F for DNO_TKAN-1...'
crit=lambda n: steklotk2F
setName='DNO_TKAN-1'
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)

print 'Calculating F for CYL-1...'
setName='CYL-1'
crit=lambda n: rovingF
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)

print 'Calculating F for DNO_ROVING...'
setName='DNO_ROVING'
crit=lambda n: rovingF
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)

print 'Calculating F for UBKA-1...'
crit=lambda n: steklotk1F
setName='UBKA-FAST'
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)

print 'Calculating F for USIL-1...'
crit=lambda n: steklotk2F
setName='USIL-FAST'
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)