# day to night mode convertor

import numpy as np

from imageio import *

import cv2

img = imread("Pythonlogo.jpg")

arr= img*np.array([0.1,0.2,0.5])

arr2 = (255*arr/arr.max()).astype(np.uint8)

imwrite('night.png',arr2)

img2= cv2.imread('night.png')

gamma = 2 # more the gamma more will be the darkness

gamma_img= np.array(255*(img2/255)**gamma,dtype='uint8')

cv2.imwrite('night_final.png',gamma_img)

print("conversion completed")
