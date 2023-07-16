# Microscope images are acquired to extract information about a sample. In order to properly quantify the information the images often need to be 
# segmented for various features of interest.

import numpy as np 
from matplotlib import pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, img_as_ubyte, io  
from scipy import ndimage  as nd # this is used for opening and closing filters
 
img = img_as_float(io.imread('E:\Research\IMG Processing\Image Processing using Python/BSE_noisy.jpg'))

# Removing Denoising from the image

sigma_est = np.mean(estimate_sigma(img, multichannel = True))
denoise = denoise_nl_means(img, h = 1.15 *sigma_est, fast_mode = True, patch_size=5, patch_distance=3,multichannel = True)

denoise_as_ubyte = img_as_ubyte(denoise)

#plt.imshow(denoise_as_ubyte, cmap='gray')

# Histogram of an image

#plt.hist(denoise_as_ubyte.flat, bins=100, range=(140,200))
#plt.savefig('Histogram-Image-L7.png', bbox_inches='tight')
#print(denoise_as_ubyte.dtype)
segmen1 = (denoise_as_ubyte <= 55)
segmen2 = (denoise_as_ubyte > 55) & (denoise_as_ubyte <= 100)
segmen3 = (denoise_as_ubyte > 100) & (denoise_as_ubyte <=140)
segmen4 = (denoise_as_ubyte > 140) & (denoise_as_ubyte <= 200)
segmen5 = (denoise_as_ubyte > 200)

# Recreating same size image to do segmentation with colors
all_segments = np.zeros((denoise_as_ubyte.shape[0], denoise_as_ubyte.shape[1], 3))

all_segments[segmen1] = (1,0,0)
all_segments[segmen2] = (0,1,0)
all_segments[segmen3] = (0,0,1)
all_segments[segmen4] = (1,1,0)
all_segments[segmen5] = (0,1,1)


segmen1_open = nd.binary_opening(segmen1, np.ones((3,3)))
segmen1_close = nd.binary_closing(segmen1_open, np.ones((3,3)))


segmen2_open = nd.binary_opening(segmen2, np.ones((3,3)))
segmen2_close = nd.binary_closing(segmen2_open, np.ones((3,3)))

segmen3_open = nd.binary_opening(segmen3, np.ones((3,3)))
segmen3_close = nd.binary_closing(segmen3_open, np.ones((3,3)))

segmen4_open = nd.binary_opening(segmen4, np.ones((3,3)))
segmen4_close = nd.binary_closing(segmen4_open, np.ones((3,3)))

segmen5_open = nd.binary_opening(segmen5, np.ones((3,3)))
segmen5_close = nd.binary_closing(segmen5_open, np.ones((3,3)))

all_segments_cleaned = np.zeros((denoise_as_ubyte.shape[0], denoise_as_ubyte.shape[1], 3))

all_segments_cleaned[segmen1_close] = (1,0,0)
all_segments_cleaned[segmen2_close] = (0,1,0)
all_segments_cleaned[segmen3_close] = (0,0,1)
all_segments_cleaned[segmen4_close] = (1,1,0)
all_segments_cleaned[segmen5_close] = (0,1,1)

#plt.imshow(all_segments_cleaned)
plt.imshow(all_segments)
plt.savefig('Histogram-Segmented-Image-L7.png', bbox_inches='tight')
plt.show()
