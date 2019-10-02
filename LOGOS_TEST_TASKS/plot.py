# %%
import matplotlib.pylab as plt
from lsmesh_lib import lsPrePost
import os
import pandas as pd
import numpy as np
from shutil import rmtree

print('Processing results...')
# %%
# task_name = 'tens11'
logos_task_path = os.path.abspath(os.path.join(
    task_name+'-log', 'task.RESULTS/D3PLOT'))
ls_task_path = os.path.abspath(task_name+'-ls')
# %%
pp = lsPrePost()

logos_command = """openc d3plot "{0}\d3plot"
ac
genselect target element
genselect element add solid 1/F1/0
newplot
etime 1
addplot
etime 2
addplot
etime 3
addplot
etime 4
addplot
etime 5
addplot
etime 6
addplot
etime 45
addplot
etime 46
addplot
etime 47
addplot
etime 48
addplot
etime 49
addplot
etime 50
xyplot 1 savefile ms_csv "{0}\\rez.csv" 1 all
"""
pp.runCommand(logos_command.format(logos_task_path))


# %%
ls_command = """ascii elout open "{0}\elout" 0
ascii elout newplot 1/2/3/4/5/6 Bk-1 Ip-1
ascii elout addplot 7 Bk-1 Ip-1
ascii elout addplot 50/51/52/53/54/55/56/57 Bk-1 Ip-1
xyplot 1 savefile ms_csv "{0}\\rez.csv" 1 all
"""
pp.runCommand(ls_command.format(ls_task_path))

# %%
logos = np.genfromtxt(os.path.join(logos_task_path, 'rez.csv'),
                      delimiter=',', skip_header=2, unpack=True)


# %%
ls = np.genfromtxt(os.path.join(ls_task_path, 'rez.csv'),
                   delimiter=',', skip_header=2, unpack=True)
# %%
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
lab = ['xx', 'yy', 'zz', 'xy', 'yz', 'xz']
for i in range(3):
    ax[0][i].plot(logos[0], logos[7+i]*100, 'r', lw=3,
                  alpha=0.7, label='ֻ־ֳ־ׁ')
    ax[0][i].grid()
    ax[0][i].set_xlabel('גנולÿ, לס', fontsize=16)
    ax[0][i].set_ylabel(r'$\varepsilon_{%s}$, %s' % (lab[i], '%'), fontsize=20)

for i in range(3):
    ax[1][i].plot(logos[0], logos[10+i]*100, 'r', lw=3,
                  alpha=0.7, label='ֻ־ֳ־ׁ')
    ax[1][i].grid()
    ax[1][i].set_xlabel('גנולÿ, לס', fontsize=16)
    ax[1][i].set_ylabel(r'$\varepsilon_{%s}$, %s' %
                        (lab[3+i], '%'), fontsize=20)

plt.tight_layout()
fig.savefig(task_name+'-fig1.png')
# %%
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
lab = ['xx', 'yy', 'zz', 'xy', 'yz', 'xz']
for i in range(3):
    ax[0][i].plot(logos[0], logos[1+i], 'r', lw=3,
                  alpha=0.7, label='ֻ־ֳ־ׁ')
    ax[0][i].plot(ls[0], ls[1+i], 'k--', label='Êֿ-1')
    ax[0][i].legend(fontsize=16)
    ax[0][i].grid()
    ax[0][i].set_xlabel('גנולÿ, לס', fontsize=16)
    ax[0][i].set_ylabel(r'$\sigma_{%s}$, ּֿא' % (lab[i]), fontsize=20)

for i in range(3):
    ax[1][i].plot(logos[0], logos[4+i], 'r', lw=3,
                  alpha=0.7, label='ֻ־ֳ־ׁ')
    ax[1][i].plot(ls[0], ls[4+i], 'k--', label='Êֿ-1')
    ax[1][i].legend(fontsize=16)
    ax[1][i].grid()
    ax[1][i].set_xlabel('גנולÿ, לס', fontsize=16)
    ax[1][i].set_ylabel(r'$\sigma_{%s}$, ּֿא' % (lab[3+i]), fontsize=20)

plt.tight_layout()
fig.savefig(task_name+'-fig2.png')
# %%
fig, ax = plt.subplots(3, 3, figsize=(15, 10))
r = 0
c = 0
for i, lab in enumerate(['1t', '2t', '3t', '1c', '2c', '3c', '12', '23', '13']):
    ax[r][c].plot(ls[0], ls[7+i])
    ax[r][c].set_xlabel('גנולÿ, לס', fontsize=16)
    ax[r][c].set_ylabel(r'$D_{%s}$' % (lab), fontsize=16)
    ax[r][c].grid()
    if c == 2:
        r += 1
        c = 0
    else:
        c += 1

plt.tight_layout()
fig.savefig(task_name+'-fig3.png')

# plt.show()
print('Done...')
# %%
rmtree(os.path.join(task_name+'-log'))
rmtree(ls_task_path)
