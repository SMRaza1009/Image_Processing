#Keypoints are points of interest in an image that can be used to compare
# images and perform tasks such as image alignment and registration. 
# These points can be automatically detected (defined) by the system using 
# algorithms such as SIFT, SURF, and ORB. Some of these algorithms can also 
# define the descriptors to make key points really useful for image 
# processing tasks. 

# Harris Corner Detection
 
 
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('E:\Research\IMG Processing\Image Processing using Python/grains2.jpg',0)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)

# harris = cv2.cornerHarris(gray, 2 , 3, 0.04)
# img[harris> 0.01*harris.max()] = [255, 0, 0]
# cv2.imshow("Harris-Corner Detection", img)
# cv2.imwrite("Harris-Corner Detection_L13.png",img)
# cv2.waitKey(0) 

#################################################################

# Shi Tomasi Corner Detection
# It is used to track good features in an image 

# corners = cv2.goodFeaturesToTrack(gray,50, 0.01,10) # 50 is detector points
# corners = np.uint(corners)
# #print(corners)

# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(img,(x,y), 3, 255, -1)
    
# cv2.imshow("Shi Tomasi Corner Detection", img)
# cv2.imwrite("Shi Tomasi Corner Detection_L13.png",img)
# cv2.waitKey(0) 

#################################################################
# This is key point detectors Harris and Shi Tomasi
# SIFT = Scale Invariant Feature Transform 
# SIFT and SERVE both are detectors and a descriptors because have the
# the information of key points and also has info about the description
# of these key points. SIFT and SERVE not available on OpenCV 3 but available on OpenCV 2


####################################################################

# Fast corner detection algorithm 
# Fast = Features Accelerated Segmented Test


# detector = cv2.FastFeatureDetector_create(50) # Detects 50 points
# kp = detector.detect(img, None)

# img2 = cv2.drawKeypoints(img, kp, None, flags=0)

# cv2.imshow("Fast Corner Detection_", img2)
# cv2.imwrite("Fast Corner Detection_L13.png", img2)
# cv2.waitKey(0)
################################################################################################

# FAST Detectot
# BRIEF descriptor
 
# ORB is combination of FAST and BRIEF (Oriented FAST and Rotated BRIEF)

orb = cv2.ORB_create(50)

kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img2), plt.show()
cv2.imwrite('ORB Image L13.png',img2)




 