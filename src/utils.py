import numpy as np
import pandas as pd

def geometric_adstock(series: np.ndarray, alpha: float) -> np.ndarray:
    
    n = len(series)

    adstocked_var = np.empty(n)
    
    adstocked_var[0] = series[0]

    for i in range(1, n):
        adstocked_var[i] = alpha * adstocked_var[i-1] + series[i]
    
    return adstocked_var
    

def saturation(x: np.ndarray, lmd: float) -> np.ndarray:
    return (1-np.exp(-lmd*x)) / (1+np.exp(-lmd*x))

def mean_scaling(df: pd.DataFrame, variables: list[str]) -> pd.DataFrame:
    """
    Mean scaling the variables.
    """
    for var in variables:
        df[var + '_scaled'] = df[var] - df[var].mean()
    return df
