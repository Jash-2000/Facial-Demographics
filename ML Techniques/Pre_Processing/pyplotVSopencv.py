# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:34:13 2020

@author: bhargav Pandya
"""

'''
    Difference in the plotting pattern of OpenCV and Matplotlib.
    
    The Ipython command
'''

import cv2
import matplotlib.pyplot as plt
from IPython import get_ipython




img = cv2.imread('Capture.PNG') 

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('uffsdfv',img)
get_ipython().run_line_magic('matplotlib', 'inline')
displays = plt.imshow(img)
plt.show()



grey =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(grey)
get_ipython().run_line_magic('matplotlib', 'qt')
display = plt.imshow(grey, cmap = 'gray')
plt.show()


cv2.imshow('ufffv',grey)

cv2.waitKey(0)
cv2.destroyAllWindows()