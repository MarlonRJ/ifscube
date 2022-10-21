from ifscube import Cube
from astropy.io import fits
from astropy import wcs
import numpy as np


r =5 # radius
coord  = np.empty(shape=[0, 2],dtype='int64')

x = np.linspace(140, 200, 4,dtype='int64')
y = np.linspace(190, 235, 3,dtype='int64')



for i in range(4):
    for j in range(3):
        aux = np.array([x[i],y[j]],dtype='int64')
        coord = np.append(coord,[aux], axis=0)
        

#print(coord)
april = Cube("/net/ASTRO/marlon/Documents/Programas_Astro/ifscube-master/ifscube/examples/Mrk_739_deep_cube.fits", scidata=1, primary=0,variance = 'STAT')

      
#list =np.array( [[140, 190], [154,212] ,[192,203] ], dtype='int64')


h = fits.HDUList()
spec = april.aperture_spectrum(x0=coord[0,0], y0=coord[0,1], radius=r)
h.append(fits.PrimaryHDU(header=spec.header))
h.append(fits.ImageHDU(data=spec.data, header=april.wcs.to_header()))
h.append(fits.ImageHDU(data=spec.variance, header=april.wcs.to_header()))

for row in range(coord.shape[0]):
    spec = april.aperture_spectrum(x0=coord[row,0], y0=coord[row,1], radius=r)
    h[1].data = spec.data.data
    h[2].data = spec.variance.data
    name ="mrk739_deep_cube_spec_"+str(coord[row,0])+"_"+str(coord[row,1])+".fits"
    h.writeto(name,overwrite=True)


