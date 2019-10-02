import os
from shutil import rmtree
from subprocess import Popen
from threading import Thread
import time
import json
from lsmesh_lib import model
import numpy as np

mesh = model('USERMAT.kk')
# task = {'name': 'tens11',
#         'eps': {'11': [0, 0.012, 0.012],
#                 '22': [0, 0, -0.015]
#                 }
#         }
Npoints = len(list(task['eps'].values())[0])
t = np.linspace(0, 1, Npoints)


kw_prescribed_motion = """*BOUNDARY_PRESCRIBED_MOTION_NODE
$#    dsid       dof       vad      lcid        sf       vid     death     birth
{ndid:10d}{dof:10s}         2{lcid:10d}       1.0         01.00000E28       0.0
"""
kw_spc_node = """*BOUNDARY_SPC_NODE
$#    ndid       cid      dofx      dofy      dofz     dofrx     dofry     dofrz
{ndid:10d}         0         1         1         1         0         0         0
"""
kw_curve = """*DEFINE_CURVE
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp     lcint
{lcid:10d}         0       1.0       1.0       0.0       0.0         0         0
$#                a1                  o1
"""


def form_motion_cards():
    rez = kw_spc_node.format(ndid=1)
    cn = 1
    for n in [2, 3, 4, 5, 6, 7, 8]:
        crds = mesh.nds[n].crds
        for i in '123':
            u = 0
            for j in '123':
                idx = [i, j]
                idx.sort()
                idx = ''.join(idx)
                eps = task['eps'].get(idx, [0]*Npoints)
                eps = np.array(eps)
                u += eps*crds[int(j)-1]
            rez += kw_curve.format(lcid=cn)
            for tt, uu in zip(t, u):
                rez += '{:20.5e}{:20.5e}\n'.format(tt, uu)
            rez += kw_prescribed_motion.format(ndid=n, dof=i, lcid=cn)
            cn += 1
    return rez


logos_params = """task {task_dir}
num      000
obschet  0
stepout  1000
outfmt   1
geom     3
sa_paral 4
nthreads 1
input    {input_file}
"""


def createTask(t):
    name = t['name']
    if os.path.exists(name+'-ls'):
        rmtree(name+'-ls')
    if os.path.exists(name+'-log'):
        rmtree(name+'-log')
    os.mkdir(name+'-ls')
    os.mkdir(name+'-log')
    open(os.path.join(name+'-ls', 'task.k'), 'w').write(
        open('MAT_221.kk', 'r').read().replace('*END', form_motion_cards()+'*END').format(**task))
    open(os.path.join(name+'-log', 'task.k'), 'w').write(
        open('USERMAT.kk', 'r').read().replace('*END', form_motion_cards()+'*END').format(**task))
    open(os.path.join(name+'-log', 'logos_sa.params'), 'w').write(
        logos_params.format(task_dir='task', input_file='task.k'))
    with open(f'{name}-ls.bat', 'w') as bat:
        bat.write(f'cd {name}-ls\n')
        bat.write(f'run_dyna i=task.k ncpus=-2 memory=200M long=s\n')
    with open(f'{name}-log.bat', 'w') as bat:
        bat.write(f'cd {name}-log\n')
        bat.write(f'logos_sa.exe\n')
    NOUT = open(os.devnull, 'w')
    print('Starting task', name)
    p1 = Popen(f'{name}-ls.bat', stdout=NOUT)
    p2 = Popen(f'{name}-log.bat', stdout=NOUT)
    p1.communicate()
    p2.communicate()
    os.remove(f'{name}-ls.bat')
    os.remove(f'{name}-log.bat')
    return name, p1, p2


createTask(task)
print('Solution done...')
