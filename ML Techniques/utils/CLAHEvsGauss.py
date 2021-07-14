# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 06:20:06 2020

@author: bhargav Pandya
"""

import cv2

img = cv2.imread('jash.jpg',0)

blur = cv2.GaussianBlur(img,(5,5),0)

imge = cv2.equalizeHist(img)
image = cv2.equalizeHist(blur)

cv2.imshow("original",img)
cv2.imshow("Direct equalization",imge)
cv2.imshow("blurred equalization",image)


clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(7,7))
cl = clahe.apply(img)

cl2 = clahe.apply(blur)
cv2.imshow("CLAHE", cl)
cv2.imshow("CLAHE Blur", cl2)

cv2.waitKey(0)
    
cv2.destroyAllWindows() 

'''
ori = cv2.imread("download.jpg",0)
gauss = cv2.GaussianBlur(ori,(5,5),0)
equ = cv2.equalizeHist(gauss)




clahe = cv2.equalizeHist(ori)
median = cv2.GaussianBlur(clahe,(5,5),0)
#clahe = cv2.CLAHE(ori)


cv2.imshow('Original',ori)
cv2.imshow('Equalized',equ)
cv2.imshow('Median Blur',median)
cv2.imshow('dd',gauss)
cv2.imshow('CLAHE',clahe)
   '''                                         # this is like the destructor function.