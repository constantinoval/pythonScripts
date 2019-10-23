import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from itertools import cycle
import vtkplotter as vtk
from usefull_features import group_by
import numpy as np
import scipy.optimize as opt


p = vtk.Plotter(shape=(1, 2), bg='white', axes=1)
a = vtk.load('tayl.stl')
sc = [c[1] for c in a.getPoints()]
a.pointColors(sc)
b = a.ybounds()
i = a.isolines(200, b[0], b[1])
i2 = a.isolines(50, b[1]*0.7, b[1]).clean()
ii = i.clean()
ii2 = i2.clean()
pnts1 = np.array([tuple(p) for p in ii.getPoints()], dtype=[
    ('x', float), ('y', float), ('z', float)])
pnts2 = np.array([tuple(p) for p in ii2.getPoints()], dtype=[
    ('x', float), ('y', float), ('z', float)])
g1 = group_by(pnts1, by='y', crit=1e-3)
g2 = group_by(pnts2, by='y', crit=1e-3)
p.show(a, i, i2, at=0, N=2)
p.show(vtk.Points(ii.getPoints()), vtk.Points(i2.getPoints()),
       vtk.Points(g1[10].tolist(), c='green'),
       vtk.Points(g1[0].tolist(), c='red'), at=1, interactive=True)

N = 10
z = []
r = []
for g in g1+g2:
    if len(g) < 10:
        continue

    def residuals(p):
        rez = []
        for point in g:
            rez.append((point['x']-p[0])**2+(point['z']-p[1])**2-p[2]**2)
        return rez
    task = opt.least_squares(residuals, [0, 0, 1], bounds=[
        [-np.inf, -np.inf, 0], [np.inf, np.inf, np.inf]])
    print(task.x)
    c = mpatches.Circle([0, 0], task.x[2], fill=False, color='k', lw=2)
    plt.gca().add_artist(c)
    plt.plot(g['x']-task.x[0], g['z']-task.x[1], '.')
    z.append(g[0]['y'])
    r.append(task.x[2])


plt.grid()
plt.gca().set_aspect('equal', 'box')
plt.figure()
plt.plot(z[:-1], r[:-1], 'o')
# plt.ylim(0, 12)
plt.show()
