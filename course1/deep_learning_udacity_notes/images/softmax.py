#%%
from unittest import result
import numpy as np
# %%
def softmax(L):
    expL = np.exp(L)
    sumExpl = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpl)
    return result

