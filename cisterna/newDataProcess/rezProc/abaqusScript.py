from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup
import caeXmlObjects.kernel.mainXML
import sys

executeOnCaeStartup()

caeXmlObjects.kernel.mainXML.loadXMLRecords(fileName='settings.xml',
                                            className='caeXmlObjects.displayGroups.dgXML.DGXML', silentMode=False,
                                            outputType='File')
caeXmlObjects.kernel.mainXML.loadXMLRecords(fileName='settings.xml',
                                            className='caeXmlObjects.paths.pathXML.PathXML', silentMode=False,
                                            outputType='File')
caeXmlObjects.kernel.mainXML.loadXMLRecords(fileName='settings.xml',
                                            className='caeXmlObjects.xyData.xyDataXML.XYDataXML', silentMode=False,
                                            outputType='File')
caeXmlObjects.kernel.mainXML.loadXMLRecords(fileName='settings.xml',
                                            className='caeXmlObjects.viewCuts.viewCutXML.ViewCutXML',
                                            silentMode=False, outputType='File')
caeXmlObjects.kernel.mainXML.loadXMLRecords(fileName='settings.xml',
                                            className='caeXmlObjects.freeBodies.fbXML.FBXML', silentMode=False,
                                            outputType='File')
caeXmlObjects.kernel.mainXML.loadXMLRecords(fileName='settings.xml',
                                            className='caeXmlObjects.spectrum.spectrumXML.SpectrumXML',
                                            silentMode=False, outputType='File')
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.odbDisplay.odbDisplayXML.OdbDisplayXML',
                                           silentMode=False, recordName='ODB Display', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.basicOptions.basicOptionsXML.BasicOptionsXML',
                                           silentMode=False, recordName='Basic Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.customViews.customViewsXML.CustomViewsXML',
                                           silentMode=False, recordName='Custom Views', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.views.ViewsXML.ViewsXML', silentMode=False,
                                           recordName='Views', outputType='File', isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.commonOptions.commonOptionsXML.CommonOptionsXML',
                                           silentMode=False, recordName='Common Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.contourOptions.contourOptionsXML.ContourOptionsXML',
                                           silentMode=False, recordName='Contour Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.superimposeOptions.superimposeOptionsXML.SuperimposeOptionsXML',
                                           silentMode=False, recordName='Superimpose Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.materialOrientationOptions.materialOrientationOptionsXML.MaterialOrientationOptionsXML',
                                           silentMode=False, recordName='Material Orientation Options',
                                           outputType='File', isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.plyStackPlotOptions.plyStackPlotOptionsXML.PlyStackPlotOptionsXML',
                                           silentMode=False, recordName='Ply Stack Plot Options',
                                           outputType='File', isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.symbolOptions.symbolOptionsXML.SymbolOptionsXML',
                                           silentMode=False, recordName='Symbol Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.freeBodyOptions.freeBodyOptionsXML.FreeBodyOptionsXML',
                                           silentMode=False, recordName='Free Body Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.viewCutOptions.viewCutOptionsXML.ViewCutOptionsXML',
                                           silentMode=False, recordName='View Cut Options', outputType='File',
                                           isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.xPlane.xPlaneXML.XPlaneXML',
                                           silentMode=False, recordName='X Plane', outputType='File', isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.yPlane.yPlaneXML.YPlaneXML',
                                           silentMode=False, recordName='Y Plane', outputType='File', isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.zPlane.zPlaneXML.ZPlaneXML',
                                           silentMode=False, recordName='Z Plane', outputType='File', isSave=0)
caeXmlObjects.kernel.mainXML.kernelCommand(fileName='settings.xml',
                                           className='caeXmlObjects.viewerPlotOptions.colorMapOptions.colorMapOptionsXML.ColorMapOptionsXML',
                                           silentMode=False, recordName='ColorMap Options', outputType='File',
                                           isSave=0)

session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=290, height=240)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()

o2 = session.openOdb(name='{}')
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
execfile('createPictures.py', __main__.__dict__)
sys.exit(0)