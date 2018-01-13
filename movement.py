# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:03:01 2018

@author: Shivam
"""

import os
import shutil

file=open(os.path.join('','file.txt'),'r')
for line in file:
    folder=line.strip()
    os.mkdir(''+folder)
    txt=line.strip()+'.txt'
    if (txt[:-4])==folder:
        shutil.move(''+txt,''+folder)
file.close()

print('all done!')
