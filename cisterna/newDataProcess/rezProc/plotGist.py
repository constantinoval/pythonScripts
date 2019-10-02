import numpy as np
import matplotlib.pylab as plt

def readData(fname):
    f=open(fname, 'r')
    rez=[]
    for l in f:
        if 'Ifmax' in l:
            rez.append(float(l.split('=')[-1]))
    f.close()
    r1=[]
    for i in range(0, len(rez), 3):
        r1.append(max(rez[i],rez[i+1],rez[i+2]))
    return r1
sosudParts=['BOT-1', 'BOT-1-2', 'BOT-1-3', 'BOT-2', 'BOT-2-2','BOT-2-3',
            'OBECH', 'USIL', 'UB-FAST', 'UB+OB']
colors=[{linerPlies:d}*'r'+16*'b', {linerPlies:d}*'r'+16*'b', {linerPlies:d}*'r'+16*'b', {linerPlies:d}*'r'+16*'b', {linerPlies:d}*'r'+16*'b', {linerPlies:d}*'r'+16*'b',
       {linerPlies:d}*'r'+16*'b', {linerPlies:d}*'r'+{obechPlies:d}*'b'+16*'m', 14*'g', {linerPlies:d}*'r'+{obechPlies:d}*'b'+14*'g']

for i, part in enumerate(sosudParts):
    plt.figure()
    b1=readData(part+'-F.txt')
    plt.bar(range(1,len(b1)+1), b1, color=list(colors[i]))
    plt.grid()
    plt.xlabel('Номер слоя')
    plt.ylabel('F')
    plt.title(part)
    plt.gcf().savefig('gist-%s.png' % part, )

