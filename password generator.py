# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 00:02:49 2017

@author: Shivam
"""

'''passwords are critical safety measure and far too often people make basic ones.
this program generates random passwords and saves them to a pwd.txt file for reference. 
every time the program is ran the file is overwritten to remove data. the pwd can be saved in
another file for keeping or written down somewhere else.'''

import string
import random
import sys
#import the necessary modules

orig_stdout=sys.stdout
f=open('pwd.txt','w')# open the file to save outputs to 
sys.stdout=f

you=int(input('how many passwords do you want?'))#asks user for number of passwords

for _ in range(you):#loops the function based on user inputs
    def id_generator(size=7, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        pwd= ''.join(random.choice(chars) for _ in range(size))
        print(pwd)
    id_generator()
    #function to generate pwd based on random choice of characters based on size
sys.stdout=orig_stdout
f.close()#closes the file
    


      
        

