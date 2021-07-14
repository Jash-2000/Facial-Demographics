# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:48:13 2020

@author: bhargav Pandya
"""


import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
left = cv2.CascadeClassifier('left_eye.xml')
right = cv2.CascadeClassifier('right_eye.xml')

img = cv2.imread('C:\\Users\\bhargav Pandya\\Desktop\\Capture.PNG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.1, 10)
lefteye = left.detectMultiScale(gray, 1.3, 5)
righteye = right.detectMultiScale(gray, 1.1, 10)




for (x,y,w,h) in faces:
    

    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    roi = img[y:y+h, x:x+w]
    
        
    lefteye = left.detectMultiScale(img, 1.3, 5)
    righteye = right.detectMultiScale(img, 1.1, 10)
    
    for (ex,ey,ew,eh) in righteye:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    for (lx,ly,lw,lh) in lefteye:
        cv2.rectangle(img, (lx, ly), (lx+lw, ly+lh), (0, 0, 255), 2)


#cv2.imwrite('C:\\Users\\bhargav Pandya\\Desktop\\1.1_10.PNG',img)
cv2.imshow('img',img)
cv2.imshow('cropped', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()