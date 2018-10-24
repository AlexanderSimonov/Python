# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:01:07 2017

@author: Aleksandr Simonov
Line Pattern Generator
"""
import cv2
import numpy as np
#from matplotlib import pyplot as plt
#import math

#Grey code pattern vertical
def grey_vert(w, h, bg_r, bg_g, bg_b, bin_r, bin_g, bin_b, bin_patt_n, img_type):
    for x in range(0,bin_patt_n):
        m = w // 2**x
        img = np.zeros((h,w,3), np.uint8)
        cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
        
        for y in range(0, 2**x):
           if (y%4)==1: 
             cv2.rectangle(img,(y*m,0),((y+1)*m,h),(bg_b, bg_g, bg_r),-1)
           elif (y%4)==2:
             cv2.rectangle(img,(y*m,0),((y+1)*m,h),(bg_b, bg_g, bg_r),-1)
           elif (y%4)==3:
             cv2.rectangle(img,(y*m,0),((y+1)*m,h),(bin_b, bin_g, bin_r),-1)  
           else:
             cv2.rectangle(img,(y*m,0),((y+1)*m,h),(bin_b, bin_g, bin_r),-1)    
        img_str='{}{:d}{}'.format('grey_patt_vert',x,img_type)
        cv2.imwrite(img_str, img)

#Grey code pattern vertical
def grey_gor(w, h, bg_r, bg_g, bg_b, bin_r, bin_g, bin_b, bin_patt_n, img_type):
    for x in range(0,bin_patt_n):
        m = h // 2**x
        img = np.zeros((h,w,3), np.uint8)
        cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
        
        for y in range(0, 2**x):
           if (y%4)==1: 
             cv2.rectangle(img,(0,y*m),(w,(y+1)*m),(bg_b, bg_g, bg_r),-1)
           elif (y%4)==2:
             cv2.rectangle(img,(0,y*m),(w,(y+1)*m),(bg_b, bg_g, bg_r),-1)
           elif (y%4)==3:
             cv2.rectangle(img,(0,y*m),(w,(y+1)*m),(bin_b, bin_g, bin_r),-1)  
           else:
             cv2.rectangle(img,(0,y*m),(w,(y+1)*m),(bin_b, bin_g, bin_r),-1)    
        img_str='{}{:d}{}'.format('grey_patt_gor',x,img_type)
        cv2.imwrite(img_str, img)


#binary pattern vertical
def bin_vert(w, h, bg_r, bg_g, bg_b, bin_r, bin_g, bin_b, bin_patt_n, img_type):
    for x in range(0,bin_patt_n):
        m = w // 2**x
        img = np.zeros((h,w,3), np.uint8)
        cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
        for y in range(0, 2**x):
           if (y%2)==0:
             cv2.rectangle(img,(y*m,0),((y+1)*m,h),(bin_b, bin_g, bin_r),-1)
           else:
             cv2.rectangle(img,(y*m,0),((y+1)*m,h),(bg_b, bg_g, bg_r),-1)
        img_str='{}{:d}{}'.format('bin_patt_vert',x,img_type)
        cv2.imwrite(img_str, img)
           
def bin_gor(w, h, bg_r, bg_g, bg_b, bin_r, bin_g, bin_b, bin_patt_n, img_type):
    for x in range(0,bin_patt_n):
        m = h // 2**x
        img = np.zeros((h,w,3), np.uint8)
        cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
        for y in range(0, 2**x):
           if (y%2)==0:
             cv2.rectangle(img,(0,y*m),(w,(y+1)*m),(bin_b, bin_g, bin_r),-1)
           else:
             cv2.rectangle(img,(0,y*m),(w,(y+1)*m),(bg_b, bg_g, bg_r),-1)
        img_str='{}{:d}{}'.format('bin_patt_gor',x,img_type)
        cv2.imwrite(img_str, img)

# vertical Line
def line_vert(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, img_type):
    m = w // line_fat
    for x in range(0,m):
        img = np.zeros((h,w,3), np.uint8)
        cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
        cv2.rectangle(img,(0 + x*line_fat,0),((0 + x*line_fat)+line_fat,h),(line_b,line_g,line_r),-1)
        img_str='{}{:d}{}'.format('line_vert',x,img_type)
        cv2.imwrite(img_str, img)

#gorizontal line
def line_gor(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, img_type):
    m = h // line_fat
    for y in range(0,m):
        img = np.zeros((h,w,3), np.uint8)
        cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
        cv2.rectangle(img,(0,0 + y*line_fat),(w,(0 + y*line_fat)+line_fat),(line_b,line_g,line_r),-1)
        img_str='{}{:d}{}'.format('line_gor',y,img_type)
        cv2.imwrite(img_str, img)

# vertical Line with fixed position
def line_vert_fix(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, line_step, img_type):
    img = np.zeros((h,w,3), np.uint8)
    cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
    cv2.rectangle(img,(0 + line_step,0),((0 + line_step)+line_fat,h),(line_b,line_g,line_r),-1)
    img_str='{}{:d}{}'.format('line_vert_fix',line_step,img_type)
    cv2.imwrite(img_str, img)

#gorizontal line with fixed position
def line_gor_fix(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, line_step, img_type):
    img = np.zeros((h,w,3), np.uint8)
    cv2.rectangle(img,(0,0),(w,h),(bg_b, bg_g, bg_r),-1)
    cv2.rectangle(img,(0,0 + line_step),(w,(0 + line_step)+line_fat),(line_b,line_g,line_r),-1)
    img_str='{}{:d}{}'.format('line_gor_fix',line_step,img_type)
    cv2.imwrite(img_str, img)

if __name__ == "__main__":
    w = 1024
    h = 768

    bg_r = 0 #background red value
    bg_g = 255 #background green value
    bg_b = 0 #background blue value

    line_r = 255 #line red value
    line_g = 0   #line green value
    line_b = 0   #line blue value

    img_type='.png'

    line_fat = 10   #толщина линии
    line_step = 200 #с какого пикселя изображения нарисовать линию (для line_vert_fix и line_gor_fix)
  
    grey_vert(w,h,bg_r,bg_g,bg_b,line_r,line_g,line_b, 18, img_type)
    grey_gor(w,h,bg_r,bg_g,bg_b,line_r,line_g,line_b, 18, img_type)
    #bin_gor(w,h,bg_r,bg_g,bg_b,line_r,line_g,line_b, 18, img_type)
    
 #   line_vert(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, img_type)
    
 #   line_gor(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, img_type)
    
 #   line_vert_fix(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, line_step, img_type)
 #   line_gor_fix(w, h, bg_r, bg_g, bg_b, line_r, line_g, line_b, line_fat, line_step, img_type)