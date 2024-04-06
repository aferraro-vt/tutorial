import numpy as np

def myplot(val:int):
    r = np.arange(0, 2, 0.01)
    theta = val * np.pi * r
    return theta,r