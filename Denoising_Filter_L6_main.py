# A compromise on signal to noise for speed often results in noisy microscope images. 
# These images can be denoised to extract relevant information. There are many choices for denoising algorithms in 
# Python but some are better than others.

from skimage import io, img_as_float   
from scipy import ndimage as nd  
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from matplotlib import pyplot as plt
 
 
#img = io.imread("E:/Research/IMG Processing/Image Processing using Python/denoising/noisy_img.jpg")

# Gaussain Filter
# gaussain_img = nd.gaussian_filter(img, sigma=3)
# plt.imshow(gaussain_img) # This blur the whole image and due to this we loose important information
# plt.savefig("Gaussain_filter_Img_L6.jpg", bbox_inches='tight')
# plt.show()

# Median Filter
# median_filt = nd.median_filter(img, size=3)
# plt.imshow(median_filt) 
# plt.savefig("Median_Filter_Img_L6.jpg", bbox_inches='tight')
# plt.show()

# Denoising Filter 

img = img_as_float(io.imread("E:/Research/IMG Processing/Image Processing using Python/denoising/noisy_img.jpg"))
sigma_est = np.mean(estimate_sigma(img, multichannel=True))
nlm = denoise_nl_means(img, h=1.5 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, multichannel=True)
plt.imshow(nlm)
plt.savefig("Denoising_Filter_Img_L6.jpg", bbox_inches='tight')
plt.show()