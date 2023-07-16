import cv2 
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('E:\Research\IMG Processing\Image Processing using Python/Alloy_noisy.jpg', 0)
img2 = cv2.resize(img,(450,350))

# eq_img = cv2.equalizeHist(img2)
# plt.hist(eq_img.flat, bins=100, range=(0,255))

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) # contrast limited adaptive histogram equalization CLAHE
cl_image = clahe.apply(img2)

plt.hist(cl_image.flat, bins=100, range=(100,255))

ret, thresh1 = cv2.threshold(cl_image, 190, 150, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(cl_image, 190, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(cl_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Original Image',img2)
cv2.imshow('Binary_Threshold_Image_01_L11_',thresh1)
cv2.imwrite('Binary_Threshold_Image_01_L11.png',thresh1)
cv2.imshow('Binary_Threshold_Image_02_L11_',thresh2)
cv2.imwrite('Binary_Threshold_Image_02_L11.png',thresh2)
cv2.imshow('OTSU_Threshold_Image_03_L11_',thresh3)
cv2.imwrite('OTSU_Threshold_Image_03_L11.png',thresh3)
#cv2.imwrite('CLAHE_Image_L11.png',cl_image)
cv2.waitKey(0)


