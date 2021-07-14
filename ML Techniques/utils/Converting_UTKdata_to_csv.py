# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:28:10 2020

@author: Jash Shah
"""


"""
    This code will create the CSV file for utk dataset. This data set will be stored as dataframe object and
    be uploaded to google colab.
    
"""
# This code will only be used only once to extract information from the image data set.

import re                                     #  For the image naming convention
from numpy import asarray                     #  Converting image to array format 
import numpy as np
import os                                     
import cv2
import pandas as pd

path = 'E:\\Second year\\PS-1 - Facial Demographics\\Data\\UTKFace\\'        

entries = os.listdir('E:/Second year/PS-1 - Facial Demographics/Data/UTKFace/') # Notice how the 2 paths are different
print(len(entries))             # This will print the number of images I have in the folder.
                        
print(entries[0])                   # Checking if the correct file format is retrived.


path_data = [None] * len(entries)
age = [None] * len(entries)
gender = [None] * len(entries)
race = [None] * len(entries)
image = [None] * len(entries)
r = [None] * len(entries)
g = [None] * len(entries)
b = [None] * len(entries)
grey = [None] * len(entries)
v = [None] * len(entries)
x = [None] * len(entries)
y = [None] * len(entries)


j = 0
for j in range(23708) :
    path_data[j] = path + entries[j]


i = 0
for files in entries:
    
    try:                                        # Try method will eliminate(ignore) any NaN value and go on to except method. 
        image[i] = files
        p = re.compile('\d+')
        age[i], gender[i], race[i], year = p.findall(files)
        print(age[i], gender[i], race[i], year, i)
        
        img = cv2.imread(path_data[i])
        
        
        [x_temp, y_temp, z_temp] = img.shape
        
        x[i] = x_temp
        y[i] = y_temp
        
        
        data = asarray(img)
        
        r_temp = data[:,:,0]
        r[i] = r_temp.reshape(-1)
        
        g_temp = data[:,:,1]
        g[i] = g_temp.reshape(-1)
        
        b_temp = data[:,:,2]
        b[i] = b_temp.reshape(-1)
        
        grey_img = cv2.imread(path_data[i],0)
        grey_temp = asarray(grey_img)
        grey[i] = grey_temp.reshape(-1)
        
        [h_temp,s_temp,v_temp] = cv2.COLOR_BGR2HSV(img)
        v[i] = v_temp.reshape(-1)
        
        
           
        
    except:
        pass
    

    i = i+1
    
    
csvData = { 'Image Name' : image,
    			'Age' : age,
    			'Gender' : gender,
    			'Race' : race,
    			'Red filter' : r,
    			'Green filter' : g,
    			'Blue filter' : b,
    			'Grey filter' : grey,
                'Luminosity ' : v,
                'x' : x,
                'y' : y
    }

df = pd.DataFrame(csvData)
print(df.head())

df.to_csv(r'E:\Second year\PS-1 - Facial Demographics\Data\UTKFace_csv.csv', index=False) # This is the path where I want to save my CSV file 
