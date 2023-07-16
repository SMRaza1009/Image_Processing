from PIL import Image
import glob

img = Image.open('1.jpg')


# resize_img = img.resize((200,200))
# #resize_img.save('1-resized-img.jpg')

# img.thumbnail((1200,1300))
# img.save('1-thumbnail-img.jpg')
# print(resize_img.size)

# Cropped Image

# cropped_img = img.crop((0,0,150,150))
# cropped_img = img.save('1-cropped-img-L3.jpg')


# Copying one to another image

# img1 = Image.open('2.jpg')
# img1.thumbnail((100,150))

# img_copy = img1.copy()
# img_copy.paste(img, (20,20))
# img_copy.save('3-Copying-one-to-another-image-L3.jpg')

# Image Rotation

# img90 = img.rotate(90) # we may rotate to any angle 45, 60, 90, 180
# img90.save('4-Image-rotation-L3.jpg')

# img45 = img.rotate(45) # we will lose the edges of images
# img45.save('45-Image-rotation-L3.jpg')


# img45 = img.rotate(45, expand=True) # without lossing the edges of images
# img45.save('45-Image-rotation-EdgesSaved-L3.jpg')

# FLIP image technique TOP BOTTOM

# img2 = Image.open('monkey.jpg')
# img_FL_LR = img2.transpose(Image.FLIP_LEFT_RIGHT)
# img_FL_LR.save('5-Image-Flip_left_right-L3.jpg')

# img_FL_TB = img2.transpose(Image.FLIP_TOP_BOTTOM)
# img_FL_TB.save('5-Image-Flip_top_bottom-L3.jpg')

# Converting RGB TO GREY level

# img2 = Image.open('monkey.jpg') # RGB to GRAYSCAL
# gray_img = img2.convert("L")
# gray_img.save('6-Converted_img_GRAY_L3.jpg')

# img3 = Image.open('images00.jpg')
# rgb_img = img3.convert("RGB")
# rgb_img.save('7-Converted_img_RGB_L3.jpg')

# FLIP and convert the image to grayscale

path = './test/*'

for file in glob.glob(path):
    img = Image.open(file)
    rotate_img = img.rotate(45, expand=True)
    rotate_img.save(file+'_rotatedImgs.png')
    gray_img = img.convert("L")
    gray_img.save(file+'_grayImages.jpg')
    