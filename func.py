import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_co_rated(matrix, a, b, axis):
    if axis == "index":
        s1 = matrix.loc[a, :]
        s2 = matrix.loc[b, :]
    elif axis == "columns":
        s1 = matrix.loc[:, a]
        s2 = matrix.loc[:, b]
    else:
        print("error")
        return None
    s1_mask = s1.notna()
    s2_mask = s2.notna()
    s_mask= s1_mask & s2_mask
    v1 = s1[s_mask].to_numpy()
    v2 = s2[s_mask].to_numpy()
    return v1, v2