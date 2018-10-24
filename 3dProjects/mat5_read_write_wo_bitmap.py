# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:49:05 2017

@author: Simonov Alexander
"""
from array import array
import numpy as np

def mat5write(matfile, xw, yw, zw, imageI, imageC):
   output_fileX = open(matfile+'X.byt', 'wb')
#   float_array = array('d', [3.14, 2.7, 0.0, -1.0, 1.1])
#   float_array.tofile(output_file)
   xw.tofile(output_fileX)
   output_fileX.close()
   output_fileY = open(matfile+'Y.byt', 'wb')
   yw.tofile(output_fileY)
   output_fileY.close()
   output_fileZ = open(matfile+'Z.byt', 'wb')
   zw.tofile(output_fileZ)
   output_fileZ.close()

def mat5read(matfile, xw, yw, zw):
   float_arrayX = np.fromfile(matfile+'X.byt', dtype=np.float32,count=-1)
   float_arrayY = np.fromfile(matfile+'Y.byt', dtype=np.float32,count=-1)
   float_arrayZ = np.fromfile(matfile+'Z.byt', dtype=np.float32,count=-1)
   
   ab = np.zeros(float_arrayX.size, dtype=[('var1', np.float32), ('var2', np.float32), ('var3', np.float32)])
   ab['var1'] = float_arrayX
   ab['var2'] = float_arrayY
   ab['var3'] = float_arrayZ
   #np.savetxt('112.txt', float_arrayX, fmt="%e")
   np.savetxt('111.txt',ab, fmt=" %e %e %e ")

   
float_arrayX = np.array([3.14, 2.7, 0.0, -1.0, 1.1], dtype=np.float32)
float_arrayY = np.array([3.14, 2.7, 0.0, -1.0, 1.1], dtype=np.float32)
float_arrayZ = np.array([3.14, 2.7, 0.0, -1.0, 1.1], dtype=np.float32)
mat5write('model',float_arrayX,float_arrayY,float_arrayZ,1,1)
mat5read('wei',1,2,3)