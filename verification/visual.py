import matplotlib.pylab as plt
import os
from shutil import rmtree
from subprocess import Popen
import time
import lsmesh_lib as lm
import json
from threading import Thread
import numpy as np
import matplotlib.colors as colors
from itertools import cycle
  
task_results = [f for f in os.listdir(os.curdir)  if f[-5:].upper()=='.JSON']
print(task_results)

def vis_kone(d, dmax):
    points=[[0,0],
            [d/2, -d/4*np.sqrt(2)],
            [dmax, -d/4*np.sqrt(2)]
    ]
    return list(zip(*points))
dexp = [8, 8.2, 8.5]
for rez in task_results:    
    plt.figure()
    data = json.load(open(rez, 'r'))
    x = np.array(data['xx'])
    y = np.array(data['yy'])
    if 'diam' in rez:
        y-=y.mean()
        plt.plot(y, x, '.b', markersize=3)
        plt.plot(y, -x, '.b')
    else:
        y-=max(y)
        plt.plot(x, y, '.-b')
        plt.plot(-x, y, '.-b')
    cls = cycle(colors.get_named_colors_mapping())
    for i, dd in enumerate(dexp):
        c = next(cls)
        plt.axvline(-dd/2, label=str(i), color = c)
        plt.axvline(dd/2, color = c)
    plt.grid()
    plt.legend()
for rez in task_results:               
    plt.figure()
    plt.title(rez)
    data = json.load(open(rez, 'r'))
    plt.plot(data['pulses'][0], data['pulses'][1], '-')
    plt.plot(data['pulses'][0], data['pulses'][2], '-')
plt.show()
                 