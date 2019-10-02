import os
from math import ceil
from shutil import copy
from subprocess import Popen

hr = 0.66666667
def createTask(task):
    plies = {'linerPlies': int(task.split('-')[-2]),
             'obechPlies': ceil(int(task.split('-')[-1]) / hr)}
    open(os.path.join(task, 'calcAllFs.py'), 'w').write(open('rezProc/calcAllFs.py','r').read().format(**plies))
    open(os.path.join(task, 'plotGist.py'), 'w').write(open('rezProc/plotGist.py','r').read().format(**plies))
    open(os.path.join(task, 'abaqusScript.py'), 'w').write(open('rezProc/abaqusScript.py','r').read().format(task+'.odb'))
    for f in ['abaqus_2018.gpr', 'calcF.py', 'createDocx.py', 'createPictures.py', 'excludeFasteners.py',
              'saveFasteners.py', 'settings.xml']:
        copy(os.path.join('rezProc', f), os.path.join(task, f))

    taskAbsPath=os.path.abspath(task)
#    with open(f'tmp-{task}.bat', 'w') as bat:
#        bat.write('cd {}\n'.format(taskAbsPath))
#        bat.write('abaqus cae script=abaqusScript.py\n')

#    return Popen(f'tmp-{task}.bat', shell=True)
    with open(f'tmp-{task}.bat', 'w') as bat:
        bat.write('cd {}\n'.format(taskAbsPath))
        bat.write('python plotGist.py\n')
        bat.write(f'python createDocx.py {task}.docx\n')
    os.system(f'tmp-{task}.bat')
#processes=[]
for t in ['g4x1-4-8', 'g4x1-4-9', 'g4x1-5-8', 'g4x1-5-9',
             'P04MPa-4-8', 'P04MPa-4-9', 'P04MPa-5-8', 'P04MPa-5-9']:
    print(f'Starting process {t}...')
    createTask(t)
#    processes.append(createTask(t))
#for p in processes:
#    p.communicate()
