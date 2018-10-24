# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:52:03 2018

@author: Simonov Alexander
"""

import time
import cv2
camera_port = 0
camera = cv2.VideoCapture(camera_port)
#time.sleep(0.0001)  # If you don't wait, the image will be dark
return_value, image = camera.read()
cv2.imwrite("opencv2.png", image)
del(camera)  # so that others can use the camera as soon as possible