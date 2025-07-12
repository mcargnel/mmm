import pandas as pd
import numpy as np
from typing import List, Dict, Union

class LinearRegression:
    """
    A simple linear regression implementation with statistical inference.
    
    Attributes:
        df (pd.DataFrame): Input dataframe
        y (str): Name of target variable
        x (List[str]): List of predictor variable names
    """
    
    def __init__(self,
                 df: pd.DataFrame,
                 y: str,
                 x: List[str]):
        """
        Initialize LinearRegression model.
        
        Args:
            df: Input dataframe
            y: Name of target variable column
            x: List of predictor variable column names
        """
        self.df = df
        self.y = y
        self.x = x
        self._fitted = False
        self._results = None

    def fit(self) -> Dict[str, Union[List[str], np.ndarray]]:
        """
        Fit the linear regression model.
        
        Returns:
            Dictionary containing regression results
        """
        # Validate inputs
        if self.y not in self.df.columns:
            raise ValueError(f"Target variable '{self.y}' not found in dataframe")
        
        missing_vars = [var for var in self.x if var not in self.df.columns]
        if missing_vars:
            raise ValueError(f"Variables not found: {missing_vars}")
        
        if len(self.df) < len(self.x) + 1:
            raise ValueError("Not enough observations for the number of variables")
        
        X = self.df[self.x].values  
        y_values = self.df[self.y].values

        # add a constant column (intercept)
        X_with_intercept = np.column_stack([X, np.ones(X.shape[0])])
        vars_names = self.x + ['intercept']
        
        # calculate the beta coefficients
        beta_hat = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ y_values
        y_hat = X_with_intercept @ beta_hat

        # calculate the mean squared error
        mse_value = self._mse(y_values, y_hat)

        se = np.sqrt(mse_value * np.diag(np.linalg.inv(X_with_intercept.T @ X_with_intercept)))
        t_values = beta_hat / se

        p_values = 2 * (1 - self._t_cdf_approx(np.abs(t_values), len(self.df) - len(self.x) - 1))

        # Create a dictionary with the results
        results = {
            'variables': vars_names,
            'beta_hat': beta_hat,
            'se': se,
            't_values': t_values,
            'p_values': p_values
        }

        self._fitted = True
        self._results = results
        return results
    
    def summary(self):
        """Print regression summary"""
        if not self._fitted:
            raise ValueError("Model must be fitted before printing summary")
        self._print_linear_regression_results(self._results)
    
    def get_coefficients(self) -> Dict[str, float]:
        """Get coefficients as dictionary"""
        if not self._fitted:
            raise ValueError("Model must be fitted before getting coefficients")
        return self._get_coeficients(self._results)
    
    @property
    def is_fitted(self) -> bool:
        """Check if model has been fitted"""
        return self._fitted
    
    def _mse(self, y: np.ndarray, y_hat: np.ndarray) -> float:
        """Calculate the mean squared error."""
        return np.mean((y - y_hat) ** 2)

    def _t_cdf_approx(self, x: np.ndarray, degrees_of_freedom: int) -> np.ndarray:
        """Approximate t-distribution CDF using normal approximation"""
        if degrees_of_freedom > 30:
            return 0.5 * (1 + np.sign(x) * np.sqrt(1 - np.exp(-2 * x**2 / np.pi)))
        else:
            raise ValueError("Degrees of freedom must be greater than 30")

    def _print_linear_regression_results(self, results: dict):
        """Print a formatted summary table of the linear regression results."""
        print("Linear Regression Results:")
        print("=" * 80)
        print(f"{'Variable':<15} {'Coefficient':<12} {'Std Error':<12} {'t-value':<10} {'p-value':<10}")
        print("-" * 80)
        
        for i, var in enumerate(results['variables']):
            coef = results['beta_hat'][i]
            std_err = results['se'][i]
            t_val = results['t_values'][i]
            p_val = results['p_values'][i]
            
            if p_val < 0.001:
                p_str = f"{p_val:.2e}"
            else:
                p_str = f"{p_val:.6f}"
                
            print(f"{var:<15} {coef:<12.6f} {std_err:<12.6f} {t_val:<10.6f} {p_str:<10}")
        
        print("=" * 80)
        print(f"Degrees of Freedom: {len(self.df) - len(self.x) - 1}")
        print(f"Number of Observations: {len(self.df)}")

    def _get_coeficients(self, results: dict) -> Dict[str, float]:
        """Get the coefficients from the results."""
        coef_names = results['variables']
        coef = results['beta_hat']
        return {coef_names[i]: coef[i] for i in range(len(coef_names))}

if __name__ == "__main__":
    print("LinearRegression class loaded successfully!")