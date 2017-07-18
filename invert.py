import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits as ap
import sys

print "Opening %s..." % sys.argv[1]
try:
    fits_file = ap.open(sys.argv[1])
    print "Successfully opened file. Don't forget to close on exit?"
except IOError:
    sys.exit("Invalid file, exiting")

np.set_printoptions(formatter={'int':hex})

print fits_file.info()
print fits_file[0].data

img_data = fits_file[0].data
print np.amin(img_data),np.amax(img_data),type(img_data[0,0])
log_data = np.log10(img_data)
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.imshow(log_data, cmap='gray_r')
plt.axis('off')
fig.savefig('lol.png', bbox_inches='tight')
