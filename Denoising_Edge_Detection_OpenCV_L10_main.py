import cv2
import numpy as np  
from matplotlib import pyplot as plt


# img = cv2.imread('E:\Research\IMG Processing\Image Processing using Python/BSE_Google_Noisy.jpg')
img = cv2.imread('E:\Research\IMG Processing\Image Processing using Python/Neuron.jpg')
img2 = cv2.resize(img,(400,300))

# kernel = np.ones((3,3), np.float32)/9 # Defining kernel
# filt_2D= cv2.filter2D(img2, -1, kernel) # Applying filter
# blur_img = cv2.blur(img2, (3,3)) # Blurring image
# gaussain_blur= cv2.GaussianBlur(img2,(3,3),0) # Applying gaussian blur 
# median_filt = cv2.medianBlur(img2, 3) # Applying median filter to retain the edges of an image 
# bilateral_filt = cv2.bilateralFilter(img2, 9, 75, 75) # Very good for noise removing and retain edge detection 9 is kernel size and 75 is path size how much fast does kernel processing

canny_edge = cv2.Canny(img2, 100, 200) # 100 minimum and 200 maximum value for edge detection

cv2.imshow('Original Image  ', img2)
cv2.imshow('Canny Edge Detection', canny_edge)
# cv2.imshow('2D Custom Image  ', filt_2D)
# cv2.imshow('Blur Image', blur_img)
# cv2.imshow('Gaussian Blur Image', gaussain_blur)
# cv2.imshow('Median Filter', median_filt)
# cv2.imshow('Bilateral Filter', bilateral_filt)

cv2.waitKey(0)
