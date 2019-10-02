import os
frez=open('approximations.txt', 'w')
for f in os.listdir(os.curdir):
    if f.startswith('out'):
        frez.write('------------------------------\n')
        execfile('approx_one_case.py', {'fname': f,
                                        'frez': frez})
        frez.write('------------------------------\n')
frez.close()
