# system
import os
import warnings
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm

import scipy


def perm_rel_change(df, label):
    perm_arr = itertools.permutations(df[label].reset_index(drop=True), 2)
    perm_arr = pd.DataFrame(np.array(list(perm_arr)))
    return perm_arr


def keep_finite(df):
    df[df == np.inf] = np.nan
    df[df == -np.inf] = np.nan
    df = df.dropna(how='any')
    return df


def cohen_d(x, y):
    y_bar = np.mean(y)
    x_bar = np.mean(x)
    n_x = len(x)
    n_y = len(y)
    s_x = np.std(x)
    s_y = np.std(y)
    s = np.sqrt(
        ((n_x - 1) * s_x ** 2 + (n_y - 1) * s_y ** 2) / (n_x + n_y - 2)
    )
    d = (y_bar - x_bar) / s
    return d


def mad(x, c=1.4826):
    return c * np.median(np.abs(x - np.median(x)))


def pmad(x, y):
    n_x = len(x)
    n_y = len(y)
    mad_x = mad(x)
    mad_y = mad(y)
    pmad = np.sqrt(
        ((n_x - 1) * mad_x ** 2 + (n_y - 1) * mad_y ** 2) / (n_x + n_y - 2)
    )
    return pmad


def get_gamma(x, y, p=50):
    return np.abs(np.percentile(y, p) - np.percentile(x, p)) / pmad(x, y)
