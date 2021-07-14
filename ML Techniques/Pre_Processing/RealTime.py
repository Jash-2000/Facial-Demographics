# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:11:59 2020

@author: Jash Shah
"""


import cv2

'''
import numpy as np 
from matplotlib import pyplot as plt 
   
      
def get_pixel(img, center, x, y): 
      
    new_value = 0
      
    try: 
        # If local neighbourhood pixel  
        # value is greater than or equal 
        # to center pixel values then  
        # set it to 1 
        if img[x][y] >= center: 
            new_value = 1
              
    except: 
        # Exception is required when  
        # neighbourhood value of a center 
        # pixel value is null i.e. values 
        # present at boundaries. 
        pass
      
    return new_value 
   
# Function for calculating LBP 
def lbp_calculated_pixel(img, x, y): 
   
    center = img[x][y] 
   
    val_ar = [] 
      
    # top_left 
    val_ar.append(get_pixel(img, center, x-1, y-1)) 
      
    # top 
    val_ar.append(get_pixel(img, center, x-1, y)) 
      
    # top_right 
    val_ar.append(get_pixel(img, center, x-1, y + 1)) 
      
    # right 
    val_ar.append(get_pixel(img, center, x, y + 1)) 
      
    # bottom_right 
    val_ar.append(get_pixel(img, center, x + 1, y + 1)) 
      
    # bottom 
    val_ar.append(get_pixel(img, center, x + 1, y)) 
      
    # bottom_left 
    val_ar.append(get_pixel(img, center, x + 1, y-1)) 
      
    # left 
    val_ar.append(get_pixel(img, center, x, y-1)) 
       
    # Now, we need to convert binary 
    # values to decimal 
    power_val = [1, 2, 4, 8, 16, 32, 64, 128] 
   
    val = 0
      
    for i in range(len(val_ar)): 
        val += val_ar[i] * power_val[i] 
          
    return val 
'''
face_cascade = cv2.CascadeClassifier('E:\\Second year\\PS-1 - Facial Demographics\\Extra work\\OpenCV\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    
    faces = face_cascade.detectMultiScale(img, 1.3,10)
    

    length = len(faces)
         
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi = img[y:y+h,x:x+w]
        
        edges = cv2.Canny(roi,100,20)
        imgt = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        th2 = cv2.adaptiveThreshold(imgt,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        th3 = cv2.Canny(th2,100,200)
    '''
        height, width = imgt.shape 
  
        img_lbp = np.zeros((height, width),np.uint8) 
        try:
            for i in range(0, height): 
                for j in range(0, width): 
                    img_lbp[i, j] = lbp_calculated_pixel(imgt, i, j) 
    
        except:
            pass
    '''
    try:
        cv2.imshow('crop',roi)  
        cv2.imshow('Sobel', edges)
        cv2.imshow('Binary threshold', th2)
        cv2.imshow('canny after', th3)
        cv2.imshow('LBP', img_lbp)
    except:
        pass
    
    cv2.imshow('img',img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()