# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:26:56 2017

@author: Shivam
"""

import os
import shutil
#imports the needed modules

x_file = open(os.path.join('', "output.txt"), "r")  
#opens the output text to scan for what documents a person needs to copy or move to a new directory

for image in x_file:
    #scans the output text for the files of interest
    v=str.strip(image)
    #strips any unnecessary character
    shutil.move(''+v, '')
    #moves the files, the destination folder needs to exist however so premake it