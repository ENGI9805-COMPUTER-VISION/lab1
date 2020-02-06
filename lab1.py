# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 01:32:57 2020

@author: ebrahim
"""

import cv2
import numpy as np

for k in range(1, 5):
    print(k)
    inputName = 'test' + str(k) + '.jpg'
    outputName = 'a' + str(k) + '.jpg'
    
    img = cv2.imread(inputName) # Remember to add the path for the test1.jpg
    size = img.shape
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 100, 500
    edges = cv2.Canny(gray,50,800) # The parameters are the thresholds for Canny
    
    lines = cv2.HoughLines(edges,1, np.pi / 180, 160) # The parameters are accuracies and threshold
    num = len(lines)
    for n in range(num):
        rho, theta = lines[n][0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + size[1]*(-b))
        y1 = int(y0 + size[0]*(a))
        x2 = int(x0 - size[1]*(-b))
        y2 = int(y0 - size[0]*(a))
    
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
    cv2.imwrite(outputName,img)