# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:07:13 2018

@author: Simonov Alexander
"""

import glob
a=input() #Input Path. (For example: D:/
print(glob.glob(a+'*.txt')) #Print all txt files in "Path"
