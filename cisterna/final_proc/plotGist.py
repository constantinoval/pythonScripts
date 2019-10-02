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
sosudParts=['CYL-1', 'DNO_ROVING', 'DNO_TKAN-1', 'UBKA-1', 'USIL-1']

for i, part in enumerate(sosudParts):
    plt.figure()
    b1=readData(part+'-F.txt')
    if max(b1)>=1.0:
        mx = max(b1)
        print('Превышение', part, ' max=', mx)
        b1 = [bb/mx for bb in b1]
    plt.bar(range(1,len(b1)+1), b1, color='b')
    plt.grid()
    plt.xlabel('Номер слоя')
    plt.ylabel('F')
    plt.title(part)
    plt.gcf().savefig('gist-%s.png' % part, )

