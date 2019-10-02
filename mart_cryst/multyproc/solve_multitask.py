import os
import json
import shutil
from subprocess import Popen


def createJob(jobName, pars, mat_name, mat):
    a = pars['a'] * 1000
    P = pars['P0']
    print(
        f'Creating job: {jobName} for material {mat_name}, a={a} mm, P={P} W')
    if os.path.exists(jobName):
        shutil.rmtree(jobName)
    os.mkdir(jobName)
    shutil.copyfile('cryst.cae', os.path.join(jobName, 'cryst.cae'))
    lines = open('solve_one_task.py', 'r').readlines()
    with open(f'{jobName}/script.py', 'w') as fout:
        fout.write(''.join(lines[:16]))
        fout.write('pars=' + repr(pars) + '\n')
        fout.write(f'mat_name=\'{mat_name}\'\n')
        fout.write('mat=' + repr(mat) + '\n')
        fout.write("""from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('cryst.cae')
""")
        fout.write(''.join(lines[16:]))
    with open(f'{jobName}.bat', 'w') as bat:
        bat.write(f'cd {jobName}\nabaqus cae noGUI=script.py\n')


def getResults(jobName):
    for f in os.listdir(jobName):
        if f.endswith('.txt'):
            shutil.copyfile(f'{jobName}/{f}', f)
            print(f'Job {jobName} finished...')
    shutil.rmtree(jobName)
    os.remove(f'{jobName}.bat')


PP = [0.5]  # , 0.7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aa = [0.7]  # , 0.5, 0.1, 0.05]

materials = json.load(open('materials.json', 'r'))
r0 = 6.25e-3


i = 0
nworkers = 4
workers = {}
for mat_name, mat in materials.items():
    for P0 in PP:
        for a in aa:
            if os.path.exists('%s_out_P0=%3.1f_a=%4.2f.txt' % (mat_name, P0, a)):
                print('Sciping file ', '%s_out_P0=%3.1f_a=%4.2f.txt' %
                      (mat_name, P0, a), ' because exists')
                continue
            pars = {'a': a * 1e-3, 'P0': P0,
                    'k': mat['k'], 'delta': mat['delta'], 'r0': r0}
            jobName = f'job-{i+1}'
            createJob(jobName, pars, mat_name, mat)
            p = Popen(f'{jobName}.bat', shell=False)
            workers[jobName] = p
            i += 1
            if i == nworkers:
                i = 0
                for p in workers.values():
                    p.wait()
                for j in workers:
                    getResults(j)
                workers = {}
for p in workers.values():
    p.wait()
for j in workers:
    getResults(j)
workers = {}
