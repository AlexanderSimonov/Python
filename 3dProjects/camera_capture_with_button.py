# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:56:45 2018

@author: Simonov Alexander
"""

import cv2
camera = cv2.VideoCapture(0)

while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)  
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        image_pattern=cv2.imread('test.jpg')
        cv2.imshow('patterns',image_pattern)
        print("Ok")        
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()