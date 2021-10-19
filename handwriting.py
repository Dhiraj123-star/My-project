# convert text into the handwritten text using Python

import pywhatkit as kit

import cv2

kit.text_to_handwriting("Python is awesome programming",save_to='myhandwriting.png')

img= cv2.imread('myhandwriting.png')
cv2.imshow("Text To handwriting",img)

cv2.waitKey(0)

cv2.destroyAllWindows() 




