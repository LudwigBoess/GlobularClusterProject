#!/home/matthias/anaconda3/bin/python

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


# 2D image (note: ds9 is a useful tool to visualize fits images)
image = fits.open('M13_i.fits')
data  = image[0].data
hdr   = image[0].header
print(hdr['EXPTIME'])
print(data.shape)


cropdata = data[300:700,300:700]
plt.imshow(cropdata, vmin=0, vmax=10000)
plt.xlabel('x')
plt.xlabel('y')
plt.show()

