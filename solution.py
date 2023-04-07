import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 1407630156 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) :
    alpha = 1 - p
    z=x**2
    l=len(x)
    raspr=chi2(2*l)
    c_1=raspr.ppf(alpha / 2)
    c_2=raspr.ppf(1 - alpha / 2)
    sum_z = len(z) * z.mean()
    return np.sqrt(sum_z / (17*c_2)), np.sqrt(sum_z /(17*c_1))
