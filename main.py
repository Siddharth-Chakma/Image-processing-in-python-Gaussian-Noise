import glob
from skimage import img_as_ubyte
import cv2
from PIL import Image
import numpy as np
from skimage.util import random_noise


path = "test_images/imgs/*.*"
for file in glob.glob(path):

        print(file)
        im = cv2.imread(file,1)
        im_arr = np.asarray(im)

        # random_noise() method will convert image in [0, 255] to [0, 1.0],
        # inherently it use np.random.normal() to create normal distribution
        # and adds the generated noised back to image
        noise_img = random_noise(im_arr, mode='gaussian', var=0.05 ** 2)
        noise_img = (255 * noise_img).astype(np.uint8)
        img =img_as_ubyte( Image.fromarray(noise_img))

        cv2.imwrite(file,img)
