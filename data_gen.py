import numpy as np
#import matplotlib.pyplot as plt

def f(lam , beta):
    def internal(x):
        term1 = lam*np.exp(-lam*x)
        term2 = np.exp(-(x-beta)**2)
        val = term1+term2
        return val 
    return internal 

def powerlaw(alpha , z, norm):
    def internal(e):
        val = norm*((e*(1+z))**(-alpha))
        return val 
    return internal

alpha = np.random.uniform(low = 0.5 , high= 2.5 , size = 10000)
z_val = np.random.uniform(low = 0.5 , high= 2.5 , size = 10000)
norm  = 1e-7
x = np.linspace(0.1,10,128)

data = []
param = []
for a, z in zip(alpha, z_val):
    #print(a)
    y = powerlaw(a,z, norm )(x)
    data.append(y)
    param.append([a,z])

data = np.asarray(data)
param = np.asarray(param)
np.savetxt('data/data.csv' , data)
np.savetxt('data/params.csv' , param)
data_log = np.log(data)
data_log_norm = (data_log - np.mean(data_log))/np.var(data_log)
np.savetxt('data/data_log_norm.csv' , data_log_norm)

