import cv2

#img = cv2.imread('E:\Research\IMG Processing\Image Processing using Python/RGBY.jpg', 1)
img = cv2.imread('E:\Research\IMG Processing\Image Processing using Python/monkey.jpg', 1)
#blue = img[:, :, 0] # --> B - 0
#green = img[:, :, 1] # --> G - 1
#red = img[:, :, 2] # --> R - 2
# blue, green, red =cv2.split(img)
# cv2.imshow('Blue ', blue)
# cv2.imshow('green ', green)
# cv2.imshow('Red ', red)

# b, g, r = cv2.split(img)

# img_merged = cv2.merge((b, g, r))
# cv2.imshow('Merged Image',img_merged)

resized_img = cv2.resize(img, None, fx =1, fy =1, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Original Image : ', img)
cv2.imshow('Resized Image : ', resized_img)
cv2.waitKey(0)