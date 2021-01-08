from soxs import Spectrum 
import numpy as np


alpha = np.random.uniform(low = 0.5 , high= 2.5 , size = 10000)
z_val = np.random.uniform(low = 0.1 , high= 2.5 , size = 10000)
norm  = 1e-7
emin = 0.3
emax  = 7.0
nbins = 128
data = []
param = []
i = 0
for a, z in zip(alpha, z_val):
    #print(a)
    spec = Spectrum.from_powerlaw(a, z , norm, emin, emax, nbins)
    _ , flx = spec.ret_spectrum_krn()
    data.append(flx)
    param.append([a,z])
    if(i%25==0):
        print('Generating data for iteration:' , i)
    i+=1

data = np.asarray(data)
param = np.asarray(param)
np.savetxt('data/data_spectrum.csv' , data)
np.savetxt('data/params_spectrum.csv' , param)
data_log = np.log(data)
data_log_norm = (data_log - np.mean(data_log))/np.var(data_log)
np.savetxt('data/data_log_norm_spectrum.csv' , data_log_norm)
