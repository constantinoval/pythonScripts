from odbAccess import *
from math import sqrt
from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup
import json
executeOnCaeStartup()
#-------------
frameToSave=1
#-------------
odb = session.odbs.values()[-1]
leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    connectorDisplay=ON)
session.writeFieldReport(fileName='fasteners.txt', append=OFF,
    sortItem='Element Label', odb=odb, step=0, frame=frameToSave,
    outputPosition=WHOLE_ELEMENT, variable=(('CTF', WHOLE_ELEMENT, ((COMPONENT,
    'CTF1'), (COMPONENT, 'CTF2'), (COMPONENT, 'CTF3'), )), ))

f=open('fasteners.txt','r')
fsh=-1e10
fn=-1e10
l=''
while(l!='-----------------------------------------------------------------\n'):
    l=f.readline()
l=f.readline()
N=0.0
fn_mean=0
fsh_mean=0
while(l.strip()):
    f1,f2,f3=list(map(float, l.split()[1:]))
    fn=max(fn, abs(f3))
    fn_mean+=abs(f3)
    fsh=max(fsh, sqrt(f1**2+f2**2))
    fsh_mean+=sqrt(f1**2+f2**2)
    N+=1
    l=f.readline()
f.close()
fn_mean=fn_mean*1.0/N
fsh_mean=fsh_mean*1.0/N

print '\n\n\n'
print 'fn_max=', 'fsh_max='
print fn, fsh
print 'fn_mean=', 'fsh_mean='
print fn_mean, fsh_mean
rez={'fn_max': fn, 'fsh_max': fsh, 'fn_mean': fn_mean, 'fsh_mean': fsh_mean}
json.dump(rez, open('fasteners.json', 'w'))
r = 20e-3/2.
h = 30.2e-3
st=230e6
ssh=115e6
ssm_ub = 47.6e6
ssm_usil = 61e6

st_max = fn/3.14/r**2
ssh_max = fsh/3.14/r**2
ssm_max = fsh/2./r/h

print '\n\n'
print 'st_max=', 'ssh_max=', 'ssm_max='
print st_max, ssh_max, ssm_max
print 'K_st_max=', 'K_ssh_max=', 'K_ssm_max_ub=', 'K_ssm_max_usil='
print st/st_max, ssh/ssh_max, ssm_ub/ssm_max, ssm_usil/ssm_max

st_mean = fn_mean/3.14/r**2
ssh_mean = fsh_mean/3.14/r**2
ssm_mean = fsh_mean/2./r/h

print '\n\n'
print 'st_mean=', 'ssh_mean=', 'ssm_mean='
print st_mean, ssh_mean, ssm_mean
print 'K_st_mean=', 'K_ssh_mean=', 'K_ssm_mean_ub=', 'K_ssm_mean_usil='
print st/st_mean, ssh/ssh_mean, ssm_ub/ssm_mean, ssm_usil/ssm_mean
