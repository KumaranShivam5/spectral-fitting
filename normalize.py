import numpy as np
def log_norm(data):
    data_log = np.log(data)
    data_log_norm = (data_log - np.mean(data_log))/np.var(data_log)
    return data_log_norm