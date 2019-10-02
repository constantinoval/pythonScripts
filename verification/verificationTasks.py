import os
from shutil import rmtree
from subprocess import Popen
import time
import lsmesh_lib as lm
import json
from threading import Thread
import numpy as np

materials = {
    'ak4': """*MAT_MODIFIED_JOHNSON_COOK_TITLE
AK-4-1
$#     mid        ro         e        pr      beta       xsi        cp     alpha
        11    0.0028   72000.0      0.33       0.0       0.9     797.0       0.0
$#   e0dot        tr        tm        t0     flag1     flag2
     0.001     293.0     933.0     293.0       1.0       0.0
$#  a/siga       b/b   n/beta0   c/beta1      m/na
     282.0     224.0    0.00643.50000E-4       0.0
$#    q1/a      c1/n q2/alpha0 c2/alpha1
     625.0      0.56   0.002261.23000E-4
$#   dc/dc     pd/wc     d1/na     d2/na     d3/na     d4/na     d5/na
       0.0       0.0      0.00      0.00       0.0    0.0000       0.0
$#      tc      tauc
1.00000E12      1e12
*PART
$#                                                                         title
sample
$#     pid     secid       mid     eosid      hgid      grav    adpopt      tmid
         3         2        11         0         0         0         0         0
""",
    'vgl12': """*MAT_JOHNSON_COOK_TITLE
VGL12U-VI
$#     mid        ro         g         e        pr       dtf        vp    rateop
        11    0.0078   78125.0  200000.0      0.28       0.0       1.0       4.0
$#       a         b         n         c         m        tm        tr      epso
     781.0    3610.0       1.3     0.039       0.0    2000.0     293.0     0.001
$#      cp        pc     spall        it        d1        d2        d3        d4
     500.0       0.0       2.0       0.0       0.0       0.0       0.0       0.0
$#      d5      c2/p      erod     efmin
      0.00      0.09         0      0.01
*EOS_LINEAR_POLYNOMIAL_TITLE
VGL12U-VI
$#   eosid        c0        c1        c2        c3        c4        c5        c6
        11       0.0  151515.0       0.0       0.0       0.0       0.0       0.0
$#      e0        v0
       0.0       0.0
*PART
$#                                                                         title
sample
$#     pid     secid       mid     eosid      hgid      grav    adpopt      tmid
         3         2        11        11         0         0         0         0
"""
}

initial_temperature_card = """*INITIAL_TEMPERATURE_SET
         0{0:10.3f}
"""

tasks = {
    'kone': 'kone.k',
    'sph': 'sph.k',
    'diam1': 'diam1.k',
    'diam2': 'diam2.k'
}


def createTask(task_dir, material, task_type, stricker_v, T=293.):
    if os.path.exists(task_dir):
        rmtree(task_dir)
    os.mkdir(task_dir)
    kwds = open(tasks[task_type], 'r').read().format(stricker_v)
    kwds = kwds.replace(
        '*END', materials[material] + initial_temperature_card.format(T) + '*END')
    open(os.path.join(task_dir, tasks[task_type]), 'w').write(kwds)
    with open(f'{task_dir}.bat', 'w') as bat:
        bat.write(f'cd {task_dir}\n')
        bat.write(f'run_dyna i={tasks[task_type]} ncpus=-2 memory=200M\n')
    NOUT = open(os.devnull, 'w')
    print('Starting task', task_dir)
    p = Popen(f'{task_dir}.bat', stdout=NOUT)
    return p


def processResults(task_dir, set_number=100):
    print('Processing result in dir', task_dir)
    rez = {}
    pre_post = lm.lsPrePost()
    full_d3plot_path = os.path.abspath(os.path.join(task_dir, 'd3plot'))
    full_elout_path = os.path.abspath(os.path.join(task_dir, 'elout'))
    lscommand = f"""openc d3plot \"{full_d3plot_path}\"\n"""
    outfname = f'{task_dir}-temp.k'
    tmp_csv = f'{task_dir}-temp.csv'
    lscommand += f"""output "{outfname}" 10000 1 0 1 0 1 0 0 0 0 0 0 0 0 0 1.000000
ascii elout open \"{full_elout_path}\" 0
ascii elout plot 21 all
xyplot 1 savefile ms_csv \"{tmp_csv}\" 1 all
"""
    k_file = [fname for fname in os.listdir(
        task_dir) if fname[-2:].upper() == '.K'][0]
    pre_post.runCommand(lscommand, f'{task_dir}.cfile')
    nset = lm.read_set(k_file)[set_number]
    nset2 = lm.read_set(k_file)[set_number + 1]
    m = lm.model(outfname)
    x = []
    y = []
    xx = []
    yy = []
    for nn in nset:
        x.append(m.nds[nn].x)
        y.append(m.nds[nn].y)
    for nn in nset2:
        xx.append(m.nds[nn].x)
        yy.append(m.nds[nn].y)
    x, y = zip(*sorted(zip(x, y), key=lambda xx: xx[0]))
    os.remove(outfname)
    rez['x'] = x
    rez['y'] = y
    rez['xx'] = xx
    rez['yy'] = yy
    data = np.genfromtxt(tmp_csv, skip_header=2,
                         delimiter=',', unpack=True)[:-1]
    os.remove(tmp_csv)
    rez['pulses'] = data.tolist()
    json.dump(rez, open(f'{task_dir}-rez.json', 'w'), indent=2)
    rmtree(task_dir)
    print('Processing result in dir', task_dir, 'is done...')


if __name__ == '__main__':
    processes = {}
    task_set = []
    with open('tasks.txt', 'r') as fin:
        next(fin)
        for l in fin:
            ll = l.split()
            if len(ll) < 5:
                continue
            ll[3] = float(ll[3])
            ll[4] = float(ll[4])
            task_set.append(ll)
    task_set_iterator = iter(task_set)
    process_number = 4
    process_result_threads = []
    while True:
        if len(processes) < process_number:
            try:
                current_task = next(task_set_iterator)
                if os.path.exists(f'{current_task[0]}-rez.json'):
                    continue
                processes[current_task[0]] = createTask(*current_task)
            except StopIteration:
                pass
        finished_processes = []
        for p in processes:
            if processes[p].poll() != None:
                os.remove(f'{p}.bat')
                print(f'Task {p} is finished...')
                finished_processes.append(p)
                tr = Thread(target=processResults, args=(p,))
                process_result_threads.append(tr)
                tr.daemon = True
                tr.start()
            else:
                print(f'Task {p} in progress...')
        for p in finished_processes:
            processes.pop(p)
        if not processes:
            break
        time.sleep(10)
    print('Solutioin done. Waiting for finish process results...')
    for tr in process_result_threads:
        tr.join()
    print('All done...')
