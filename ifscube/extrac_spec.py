
from astropy.io import fits
from ifscube import datacube

#import ifscube.io.line_fit
import matplotlib.pyplot as plt
from ifscube import fitter
from ifscube import parser
from ifscube import onedspec

myspec =datacube.Cube('/net/ASTRO/marlon/Documents/Programas_Astro/ifscube-master/ifscube/examples/Mrk_739_deep_cube.fits',variance='STAT', scidata='DATA', redshift=0.02985)
myspec.rest_wavelength *= 1e+10
abel = myspec.aperture_spectrum(radius=5.0, x0=184, y0=214)

#abel = onedspec.Spectrum('/net/ASTRO/marlon/Documents/Programas_Astro/ifscube-master/ifscube/examples/mrk739_deep_cube_spec_184_214.fits', scidata=1,primary=0,redshift=0.02985)
#c = parser.LineFitParser('/home/croissant/ifscube-master/ifscube/examples/halpha_gauss.cfg')
#abel.plot()

c = parser.LineFitParser('/net/ASTRO/marlon/Documents/Programas_Astro/ifscube-master/ifscube/examples/halpha_gauss.cfg')
line_fit_args = c.get_vars()

abel_fit = fitter.spectrum_fit(abel, options={"disp": True}, **line_fit_args)

abel_fit.plot(return_results=True)


plt.show()
