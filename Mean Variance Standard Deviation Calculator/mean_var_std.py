import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    a = np.array(list)
    b = a.copy().reshape(3, 3)

    arr_mean = [b.mean(axis=0).tolist(), b.mean(axis=1).tolist(), b.reshape(1, 9).mean()]
    arr_var = [np.var(b, axis=0).tolist(), np.var(b, axis=1).tolist(), np.var(b.reshape(1, 9))]
    arr_std = [np.std(b, axis=0).tolist(), np.std(b, axis=1).tolist(), np.std(b.reshape(1, 9))]
    arr_min = [np.min(b, axis=0).tolist(), np.min(b, axis=1).tolist(), np.min(b.reshape(1, 9))]
    arr_max = [np.max(b, axis=0).tolist(), np.max(b, axis=1).tolist(), np.max(b.reshape(1, 9))]
    arr_sum = [np.sum(b, axis=0).tolist(), np.sum(b, axis=1).tolist(), np.sum(b.reshape(1, 9))]

    calculations = {
        'mean': arr_mean,
        'variance': arr_var,
        'standard deviation': arr_std,
        'max': arr_max,
        'min': arr_min,
        'sum': arr_sum
    }

    return calculations
