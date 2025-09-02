import pandas as pd
import numpy as np

# Compute ecdf function:
def ecdf(x):
    Z = np.sort(x.unique()) # Extract and sort unique values for x
    compare = x.to_numpy().reshape(-1,1) <= Z.reshape(1,-1) # Compare x and Z values
    
    ecdf = np.mean(compare,axis=0) # Average over x indices for each z

def compute_quantile(x):
    # Find median index closest to .5
    idx = np.searchsorted(F_hat, 0.5)
    if idx == 0:
        return grid[0]
    elif idx == len(F_hat):
        return grid[-1]
    # Points just below and above the 0.5 threshold:
    x0, x1 = grid[idx - 1], grid[idx]
    y0, y1 = F_hat[idx - 1], F_hat[idx]
    # Linear interpolation for median:
    t = (0.5 - y0) / (y1 - y0)
    return x0 + t * (x1 - x0)

def compute_iqr(x):
    return np.quantile(x,.75) - np.quantile(x,.25)

def compute_summary(x):
    return compute_median(x), compute_quantile(x), compute_iqr(x)

# Outliers
def test_whisker(x, low_bound, high_bound):
    if x >= low_bound and x <= high_bound:
        return True
    else:
        return False