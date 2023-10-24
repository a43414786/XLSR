import os
import glob
import shutil

BSD100PATH = 'BSD100'
URBAN100PATH = 'Urban100'
SET5PATH = 'Set5'
SET14PATH = 'Set14'

def fun(path):
    srcPath = os.path.join(path,'X2')
    cnt = 0
    for imgName in os.listdir(srcPath):
        if('HR' in imgName):
            cnt += 1
            shutil.copy(os.path.join(srcPath,imgName),os.path.join(path,'{:03d}.png'.format(cnt)))
    shutil.rmtree(srcPath)
    
fun(BSD100PATH)
fun(URBAN100PATH)
fun(SET5PATH)
fun(SET14PATH)