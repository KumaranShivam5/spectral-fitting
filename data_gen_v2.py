from soxs import Spectrum 
from matplotlib import pyplot as plt

alpha = 1.2
zobs = 0.05
norm = 1.0e-7

emin = 0.1
emax = 10.0
nbins = 256
spec = Spectrum.from_powerlaw(alpha, zobs, norm, emin, emax, nbins)
#spec.plot()
#plt.show()
data = spec.get_flux_in_band(0.1, 10.0)
#plt.plot(data)
#plt.show()
print(data)
#print(spec.shape)