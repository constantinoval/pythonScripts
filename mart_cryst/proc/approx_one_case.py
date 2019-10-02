"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import visvis as vv
import lmfit

plot=False

if plot:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
if not locals().has_key('fname'):
    fname='out_P0=0.1_a=0.05.txt'

if not locals().has_key('frez'):
    frez=open('test_out.txt','w')

conds=fname.split('_')
frez.write(conds[1] +', '+ conds[2][:-4]+'\n')
a0=float(conds[2][:-4].split('=')[1])*1e-3
data=np.loadtxt(fname, delimiter=',', skiprows=1, unpack=False)
x=[]
y=[]
t=[]
y0=[[], []]
y1=[[], []]
for d in data:
    if d[1]<=a0*5:
        x.append(d[1]+d[5])
        y.append(d[2]+d[6])
        x.append(-x[-1])
        y.append(y[-1])
        t.append(d[4])
        t.append(t[-1])
        if abs(d[2])<=1e-8:
            y0[0].append(x[-1])
            y0[0].append(-x[-1])
            y0[1].append(y[-1])
            y0[1].append(y[-1])
        if abs(d[2]-2.1e-3)<=1e-8:
            y1[0].append(x[-1])
            y1[0].append(-x[-1])
            y1[1].append(y[-1])
            y1[1].append(y[-1])
y0=np.array(y0)*1e6            
y1=np.array(y1)*1e6            
x=np.array(x)*1e3
y=np.array(y)*1e3

#def fnc2min(pars, x, data):
#    v=pars.valuesdict().values()
#    rez=[]
#    degs=((3,0), (0,3), (2,1), (1,2), (2,0), (0,2), (1,1), (1,0), (0,1),  (0,0))
#    for i, d in enumerate(data):
#        fv=0
#        for deg, k in zip(degs, v):
#            fv+=k*x[0][i]**deg[0]*x[1][i]**deg[1]
#        rez.append(fv-d)
#    return np.array(rez)
    
#def approx(x,y,pars):
#    v=pars.valuesdict().values()
#    degs=((3,0), (0,3), (2,1), (1,2), (2,0), (0,2), (1,1), (1,0), (0,1), (0,0))
#    fv=0
#    for deg, k in zip(degs, v):
#        fv+=k*x**deg[0]*y**deg[1]
#    return fv

def approx(x,y,pars):
    v=pars.valuesdict()
    rez=[]
    fv=v['a']*np.exp(-x**2/v['w1'])*np.exp(-y/v['w2'])+v['b']
    return fv

def fnc2min(pars, x, data):
    v=pars.valuesdict()
    rez=[]
    for i, d in enumerate(data):
        fv=v['a']*np.exp(-x[0][i]**2/v['w1'])*np.exp(-x[1][i]/v['w2'])+v['b']
        rez.append(fv-d)
    return np.array(rez)
    
pars=lmfit.Parameters()
pars.add('a', value=40)
pars.add('w1', value=0.4, min=0.00001)
pars.add('b', value=1600., min=0)
pars.add('w2', value=0.4, min=0.00001)

#pars=lmfit.Parameters()
#for i in xrange(10):
#    pars.add('a%d' % (i,), value=1.)
result=lmfit.minimize(fnc2min, pars, args=([x,y], t))
lmfit.report_fit(pars)
t=np.array(t)
mt=t.mean()
RR2=1-np.sum(result.residual**2)/np.sum((t-mt)**2)
print 'R^2=', RR2
frez.write('Temperature field approximation parameters [mm]:\n')
for p, v in pars.valuesdict().iteritems():
    frez.write('%s=%e\n' % (p, v))
frez.write('R^2=%f\n' % (RR2,))
if plot:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m=1.
    xxx=np.linspace(min(x)*m, max(x)*m, 100)
    yyy=np.linspace(min(y)*m, max(y)*m, 50)
    xxx,yyy=np.meshgrid(xxx,yyy)
    fncvals=[approx(xx,yy,pars) for xx, yy in zip(xxx,yyy)]
    ax.scatter(x,y,t, c='r')
    ax.plot_wireframe(xxx, yyy, fncvals)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('T')

def fnc2min2(pars, x, data):
    v=pars.valuesdict().values()
    rez=[]
    for i, d in enumerate(data):
        fv=0
        for k, p in enumerate(v):
            fv+=p*x[i]**(2*k)
        rez.append(fv-d)
    return np.array(rez)

def approx2(x, pars):
    v=pars.valuesdict().values()
    fv=0
    for k, p in enumerate(v):
        fv+=p*x**(2*k)
    return fv

appDeg=9

pars=lmfit.Parameters()
for i in xrange(0,appDeg,2):
        pars.add('a%d' % (i,), value=0)        
result=lmfit.minimize(fnc2min2, pars, args=(y0[0], y0[1]))
lmfit.report_fit(pars)
yy=np.array(y0[1][1:])
myy=yy.mean()
RR2=1-np.sum(result.residual[1:]**2)/np.sum((yy-myy)**2)
print 'R^2=', RR2
frez.write('Bottom face approximation parameters [mkm]:\n')
for p, v in pars.valuesdict().iteritems():
    frez.write('%s=%e\n' % (p, v))
frez.write('R^2=%f\n' % (RR2,))

if plot:
    xxx=np.linspace(min(y0[0]),max(y0[0]),50)
    yyy=[approx2(xxxx,pars) for xxxx in xxx]
    plt.figure()
    plt.plot(y0[0],y0[1],'o')
    plt.plot(xxx,yyy)
    plt.axvspan(-a0*1e6,a0*1e6)

pars=lmfit.Parameters()
for i in xrange(0,appDeg,2):
    pars.add('a%d' % (i,), value=1.)
result=lmfit.minimize(fnc2min2, pars, args=(y1[0], y1[1]))
lmfit.report_fit(pars)
yy=np.array(y1[1])
myy=yy.mean()
RR2=1-np.sum(result.residual**2)/np.sum((yy-myy)**2)
print 'R^2=', RR2
frez.write('Top face approximation parameters [mkm]:\n')
for p, v in pars.valuesdict().iteritems():
    frez.write('%s=%e\n' % (p, v))
frez.write('R^2=%f\n' % (RR2,))
if plot:
    plt.figure()
    plt.plot(y1[0],y1[1],'o')
    yyy=[approx2(xxxx,pars) for xxxx in xxx]
    plt.plot(xxx,yyy)
    plt.axvspan(-a0*1e6,a0*1e6)
    plt.show()
