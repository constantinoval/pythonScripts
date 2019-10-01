# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:51:23 2012

@author: Sasha
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Lasso
from matplotlib.path import Path
import sys
import json
#from matplotlib.nxutils import points_inside_poly
#from openopt import SNLE
def to_real(diagr, stress_state='c'):
    sign=[-1,1][stress_state=='t']
    diagr['er']=sign*np.log(1+sign*diagr['et'])
    diagr['sr']=diagr['st']*(1+sign*diagr['et'])
    diagr['der']=diagr['det']/(1+sign*diagr['et'])

de_stat=0.01
class myplt:
    def __init__(self,fname):
        self.fname=fname
        if 'static' in fname:
            data=np.loadtxt(fname, skiprows=1, unpack=True)
            data={'et':data[0]/100.0,'st':data[1],'det': np.array([de_stat]*len(data[0]))}
            self.static=True
            self.fname=fname[:-4]
        else:
            self.static=False
            data=json.load(open(fname,'r'))
            for k in data.keys():
                data[k]=np.array(data[k])
        self.figure=plt.figure()
        self.data=data
        self.ax=self.figure.add_subplot(111)
        self.ax.grid()
        self.ax.set_xlabel('strain')
        self.ax.set_ylabel('stress, MPa')
        self.line,=self.ax.plot(data['et'],data['st'],'.')
        self.canvas=self.figure.canvas
        self.cid=self.canvas.mpl_connect('button_press_event', self.onclick)
        self.bid=self.canvas.mpl_connect('key_press_event', self.onbutton)
        self.selected_points=None
        self.E02=None
        self.real=None
        plt.show()

    def callback(self, verts):
        p=Path(verts, closed=True)
        points=zip(*self.line.get_data())
        ind=[]
        for i, pp in enumerate(points):
            if p.contains_point(pp):
                ind.append(i)
        xs=self.data['et'][ind]
        ys=self.data['st'][ind]
        if self.selected_points:
             self.ax.lines.remove(self.selected_points)
        self.selected_points,=self.ax.plot(xs,ys,'ro')
        self.ind = ind
        self.canvas.draw_idle()
        self.canvas.widgetlock.release(self.lasso)
        del self.lasso
        
    def onclick(self,event):
        if self.canvas.widgetlock.locked(): return
        if event.inaxes is None: return
        if event.button!=1: return
        self.lasso = Lasso(event.inaxes, (event.xdata, event.ydata), self.callback)
        self.canvas.widgetlock(self.lasso)

    def onbutton(self,event):
        if event.key.upper()=='M' and self.selected_points:
            for k in self.data.keys():
                self.data[k]=self.data[k][self.ind[0]:self.ind[-1]]
            if not self.static:
                self.data['t']-=self.data['t'][0]
            self.data['et']-=self.data['et'][0]
            to_real(self.data, self.fname[0])
            self.line.set_data(self.data['er'],self.data['sr'])
            self.ax.lines.remove(self.selected_points)
            self.selected_points=None
            self.writedata()
            self.canvas.draw()
    def writedata(self):
        f=open(self.fname[:-4]+'pl', 'w')
        f.write(self.fname[0]+'\n')
        T=float(self.fname[:-4].split('-')[-1])+273
        f.write('ep s de T')
        dov=False
        if len(self.data.get('he', [])):
            f.write(' eperr serr deerr')
            dov=True
        f.write('\n')
        for i in range(len(self.data['et'])):
            f.write('{} {} {} '.format(self.data['er'][i], self.data['sr'][i],
                                         self.data['der'][i]))
            f.write(str(T))
            if dov:
                f.write(' {} {} {}'.format(self.data['he'][i], self.data['hs'][i],
                                           self.data['hde'][i]))
            f.write('\n')
        f.close()

#            np.savez_compressed(self.fname+'.npz',de=self.data['der'],e=self.data['er'],s=self.data['sr'],
#            he=self.data['he'], hs=self.data['hs'], hde=self.data['hde'])
#            self.canvas.draw()

fname=sys.argv[1]#.split('_')[0]#'t590-750-20'
mp=myplt(fname)
