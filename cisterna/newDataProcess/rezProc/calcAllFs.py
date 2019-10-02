from odbAccess import *
from calcF import calcF, createField
from math import sqrt
from collections import defaultdict

#
instance='BOCHKA_FULL-1'
frame=-1
#
#-----------
K=4
#-----------
roving=dict()
roving['s1p']=763.2e6/K
roving['s1m']=440.7e6/K
roving['s2p']=21.2e6/K
roving['s2m']=124e6/K
roving['s12']=36.67e6/K
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

steklotk=dict()
steklotk['s1p']=247.6e6/K
steklotk['s1m']=434.7e6/K
steklotk['s2p']=247.6e6/K
steklotk['s2m']=434.7e6/K
steklotk['s12']=33.65e6/K2
steklotk['s12p']=steklotk['s12m']=steklotk['s12']

steklotkF=dict()
steklotkF['F1']=1.0/steklotk['s1p']-1.0/steklotk['s1m']
steklotkF['F2']=1.0/steklotk['s2p']-1.0/steklotk['s2m']
steklotkF['F11']=1.0/steklotk['s1p']/steklotk['s1m']
steklotkF['F22']=1.0/steklotk['s2p']/steklotk['s2m']
steklotkF['F33']=1.0/steklotk['s12']**2
steklotkF['F12']=-0.5*sqrt(steklotkF['F11']*steklotkF['F22'])

for k in steklotkF.keys():
    exec(k+'='+str(steklotkF[k]))

steklotkF.update(steklotk)

steklomatF=defaultdict(lambda:0)

#------------------------------
odb=session.odbs.values()[-1]

print 'Calculating F for DNO_TKAN-1...'
crit=lambda n: steklotkF
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
crit=lambda n: steklotkF
setName='UBKA-1'
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)

print 'Calculating F for USIL-1...'
crit=lambda n: steklotkF
setName='USIL-1'
ply=calcF(odb, instance, setName, crit, frame, '%s-F.txt' % setName)
createField(odb, instance, setName, crit, ply, frame, '%s-F' % setName)