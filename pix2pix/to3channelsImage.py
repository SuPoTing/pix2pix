import sys
from skimage import io
import numpy as np
import os

# This script converts 4 channel or 1 channel image to 3 channel images.

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        print(filename)
        f2 = os.path.join(folder,filename)
        img = io.imread(f2)
        if len(img.shape) == 3:
                # If image 4 channel
                img2 = img[:,:,:3]
        else:
                # If img 1 channel grayscale
                img = np.expand_dims(img, 2)
                print(str(img.shape))
                img2 = np.concatenate((img, img, img), axis=2)
                print(str(img2.shape))

        io.imsave(f2, img2)
        # io.imsave(os.path.join(folder, 'alt-' + filename), img2)

#load_images_from_folder('./Pix2pix-frames-480p-frames10')
load_images_from_folder(sys.argv[1])
