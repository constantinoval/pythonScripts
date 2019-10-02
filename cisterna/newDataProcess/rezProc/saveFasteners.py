from odbAccess import *
from math import sqrt
from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup
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
while(l.strip()):
    f1,f2,f3=list(map(float, l.split()[1:]))
    fn=max(fn, abs(f3))
    fsh=max(fsh, sqrt(f1**2+f2**2))
    l=f.readline()
f.close()
print 'fn=', fn, ' fsh=', fsh
