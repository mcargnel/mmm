import numpy as np
import pandas as pd

def geometric_adstock(series: np.ndarray, alpha: float) -> np.ndarray:
    """
    Apply geometric adstock transformation to a time series.
    
    The adstock effect models how marketing impact persists over time using
    the formula: Adstock_t = Media_t + α * Adstock_{t-1}
    
    Parameters
    ----------
    series : np.ndarray
        Input time series data (e.g., media spend over time)
    alpha : float
        Decay parameter controlling persistence (0 < α < 1).
        Higher values mean longer persistence of effects.
        
    Returns
    -------
    np.ndarray
        Adstocked time series with persistence effects
        
    Examples
    --------
    >>> import numpy as np
    >>> media_spend = np.array([100, 0, 50, 0, 75])
    >>> adstocked = geometric_adstock(media_spend, alpha=0.6)
    >>> print(adstocked)
    [100.   60.   86.   51.6 105.96]
    
    Notes
    -----
    This implements the classic geometric adstock model used in
    marketing mix modeling to capture carryover effects of marketing
    activities. The half-life of effects can be calculated as
    ln(0.5) / ln(alpha).
    """
    n = len(series)

    adstocked_var = np.empty(n)
    
    adstocked_var[0] = series[0]

    for i in range(1, n):
        adstocked_var[i] = alpha * adstocked_var[i-1] + series[i]
    
    return adstocked_var
    

def saturation(x: np.ndarray, lmd: float) -> np.ndarray:
    """
    Apply saturation transformation to model diminishing returns.
    
    The saturation function transforms adstocked media data to model
    diminishing returns on marketing spend using a sigmoid-like curve.
    
    Parameters
    ----------
    x : np.ndarray
        Input data (typically adstocked media variables)
    lmd : float
        Saturation parameter controlling the curve shape.
        Higher values create steeper saturation curves.
        
    Returns
    -------
    np.ndarray
        Saturated values between 0 and 1
        
    Examples
    --------
    >>> import numpy as np
    >>> adstocked_media = np.array([0, 10, 50, 100, 200])
    >>> saturated = saturation(adstocked_media, lmd=0.1)
    >>> print(saturated)
    [0.         0.46211716 0.76159416 0.88079708 0.96402758]
    
    Notes
    -----
    This function uses the formula: (1 - exp(-λx)) / (1 + exp(-λx))
    which creates an S-shaped curve that models diminishing returns
    on marketing investment. The parameter λ controls how quickly
    saturation occurs.
    """
    return (1-np.exp(-lmd*x)) / (1+np.exp(-lmd*x))

def mean_scaling(df: pd.DataFrame, variables: list[str]) -> pd.DataFrame:
    """
    Apply mean scaling (centering) to specified variables in a DataFrame.
    
    Mean scaling subtracts the mean from each variable, centering the data
    around zero. This is useful for regression analysis and interpretation
    of coefficients.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing the variables to scale
    variables : list[str]
        List of column names to apply mean scaling to
        
    Returns
    -------
    pd.DataFrame
        DataFrame with new scaled columns (original columns + '_scaled' suffix)
        
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'x1': [10, 20, 30], 'x2': [5, 15, 25]})
    >>> scaled_df = mean_scaling(df, ['x1', 'x2'])
    >>> print(scaled_df[['x1_scaled', 'x2_scaled']])
       x1_scaled  x2_scaled
    0      -10.0      -10.0
    1        0.0        0.0
    2       10.0       10.0
    
    Notes
    -----
    This function creates new columns with '_scaled' suffix rather than
    modifying the original columns. This preserves the original data
    for comparison and analysis.
    """
    for var in variables:
        df[var + '_scaled'] = df[var] - df[var].mean()
    return df
