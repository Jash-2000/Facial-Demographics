import numpy as np 
from matplotlib import pyplot as plt 
   
      
def get_pixel(img, center, x, y): 
      
    new_value = 0
      
    try:  
        # If local neighbourhood pixel value is greater than or equal to center pixel values then set it to 1
        if img[x][y] >= center: 
            new_value = 1
              
    except: 
        #Values present at boundaries. 
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

  


import cv2

gray = cv2.imread("E:\\Second year\\PS-1 - Facial Demographics\\Data\\UTKFace\\110_0_0_20170112213500903.jpg.chip.jpg",0)

img = cv2.imread("E:\\Second year\\PS-1 - Facial Demographics\\Data\\UTKFace\\110_0_0_20170112213500903.jpg.chip.jpg")
b1 = cv2.GaussianBlur(img, (1,1), 3)
b2 = cv2.GaussianBlur(img, (3,3), 3)

bg1 = cv2.GaussianBlur(gray, (1,1), 3)
bg2 = cv2.GaussianBlur(gray, (3,3), 3)

th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)


hog = cv2.HOGDescriptor()
h = hog.compute(img)

cv2.imshow('h',h)


height, width = gray.shape 
   
img_lbp = np.zeros((height, width), 
                   np.uint8) 
   
for i in range(0, height): 
    for j in range(0, width): 
        img_lbp[i, j] = lbp_calculated_pixel(gray, i, j) 
  
plt.imshow(gray, cmap = "gray") 
plt.show() 
   
plt.imshow(img_lbp, cmap ="gray") 
plt.show() 


final = b1-b2
finalg = bg1-bg2
cv2.imshow("DoG",final)
cv2.imshow("DoG g",finalg)
cv2.imshow('Gray', gray)
cv2.imshow('sd',th2)
cv2.waitKey(0)
cv2.destroyAllWindows()