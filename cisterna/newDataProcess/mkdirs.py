import os
import shutil


for f in os.listdir(os.curdir):
    if f[-4:]=='.odb':
        os.mkdir(f[:-4])
        shutil.move(f, os.path.join(f[:-4], f))