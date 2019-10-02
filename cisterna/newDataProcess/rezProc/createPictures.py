from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup
from collections import defaultdict
executeOnCaeStartup()

def runScripts():
    execfile('excludeFasteners.py', __main__.__dict__)
    execfile('saveFasteners.py', __main__.__dict__)
    execfile('calcAllFs.py', __main__.__dict__)

sosudParts=['BOT-1', 'BOT-1-2', 'BOT-1-3', 'BOT-2', 'BOT-2-2','BOT-2-3',
            'OBECH', 'USIL', 'UB-FAST', 'UB+OB']
sviews=[[1], [1], [1], [2], [2], [2],
       [1,3], [1,3], [1,3], [1,3]]

ramaParts=['BALKI-1', 'KREPLENIA-MM-1', 'RAMA1-MM-1']
sosudInstance='CISTERNA-MM-SHELL-1'



session.printOptions.setValues(reduceColors=False)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step='load-step', frame=1)
print 'Mises in rama...'

def plotRama(maxS=None,     sviews=[1,2]):
    leaf = dgo.LeafFromPartInstance(partInstanceName=tuple(ramaParts))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
    session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
        averageElementOutput=False)
    session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
        sectionResults=USE_ENVELOPE)
    if maxS:
        session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
            outsideLimitsAboveColor='#000000', maxAutoCompute=OFF, maxValue=maxS)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT,
        'Mises'), )
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    for j in sviews:
        session.viewports['Viewport: 1'].view.setValues(session.views['User-{}'.format(j)])
        session.printToFile(fileName='ramaMises-{}.png'.format(j), format=PNG, canvasObjects=(
            session.viewports['Viewport: 1'], ))
        session.saveOptions(directory=CURRENT)


def plotSosudE(maxE=None, sviews=[1,2]):
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
        INVARIANT, 'Max. In-Plane Principal'), )
    if maxE:
        session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
            maxValue=maxE)
    leaf = dgo.LeafFromElementSets(elementSets=
                   tuple(map(lambda x: sosudInstance+'.'+x, sosudParts)))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
    for j in sviews:
        session.viewports['Viewport: 1'].view.setValues(session.views['User-{}'.format(j)])
        session.printToFile(fileName='emax-{}.png'.format(j), format=PNG, canvasObjects=(
            session.viewports['Viewport: 1'], ))
        session.saveOptions(directory=CURRENT)

def plotSosudF(maxF=None, sviews=defaultdict(lambda: [1])):
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='Session Step',
        frame=0)
    leaf = dgo.LeafFromPartInstance(partInstanceName=(sosudInstance, ))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
    if maxF:
        session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
            maxAutoCompute=OFF, maxValue=maxF, minValue=0)
    for i, spart in enumerate(sosudParts):
        session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel=spart+'-F', outputPosition=INTEGRATION_POINT, )
        for j in sviews[i]:
            session.viewports['Viewport: 1'].view.setValues(session.views['User-{}'.format(j)])
            session.printToFile(fileName='{}-{}.png'.format(spart, j), format=PNG, canvasObjects=(
            session.viewports['Viewport: 1'], ))
            session.saveOptions(directory=CURRENT)


runScripts()
plotRama(maxS=345, sviews=[1,2])
plotSosudE(0.002, sviews=[1,2])
plotSosudF(maxF=1, sviews=sviews)