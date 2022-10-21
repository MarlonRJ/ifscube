
from astropy.io import fits
from ifscube import datacube

#import ifscube.io.line_fit
import matplotlib.pyplot as plt
from ifscube import fitter
from ifscube import parser
from ifscube import onedspec
import os
import numpy as np

# initialization

path_cfg = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','ifscube' ,'examples', 'halpha_gauss.cfg'))
c = parser.LineFitParser(path_cfg)
line_fit_args = c.get_vars()
#myspec =datacube.Cube('/net/ASTRO/marlon/Documents/Programas_Astro/ifscube-master/ifscube/examples/Mrk_739_deep_cube.fits',variance='STAT', scidata='DATA', redshift=0.02985)
#myspec.rest_wavelength *= 1e+10
#abel = myspec.aperture_spectrum(radius=5.0, x0=184, y0=214)
#path = '/net/ASTRO/marlon/ifscube_master/ifscube/mrk739_deep_cube_spec_184_214.fits'

#coord  = np.empty(shape=[0, 2],dtype='int64')
coord = np.array([[154,212],[184,214],[192,203]],dtype='int64')
#coord = np.array([[184,214],[154,212],[192,203]],dtype='int64')
x = np.linspace(140, 200, 4,dtype='int64')
y = np.linspace(190, 235, 3,dtype='int64')



for i in range(4):
    for j in range(3):
        aux = np.array([x[i],y[j]],dtype='int64')
        coord = np.append(coord,[aux], axis=0)

#print(coord)        
for row in range(coord.shape[0]):
#for row in range(1):
    
    name_fits ='mrk739_deep_cube_spec_'+str(coord[row,0])+'_'+str(coord[row,1])+'.fits'
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','ifscube', name_fits))
    abel = onedspec.Spectrum(path, scidata=1,primary=0,variance =2,redshift=0.02985)
    abel_fit = fitter.spectrum_fit(abel, options={"disp": True}, **line_fit_args)

    abel_fit.plot(return_results=True)

    plot_fits ='mrk739_deep_cube_spec_'+str(coord[row,0])+'_'+str(coord[row,1])+'.png'
    

    plt.savefig(plot_fits,dpi = 300)

    plt.close()
