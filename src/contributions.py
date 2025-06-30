import pandas as pd

class Contributions:
    def __init__(self, df: pd.DataFrame, coefficients: dict[str, float], 
                 media_variables: list[str], media_cost_dict: dict[str, float]):
        self.df = df
        self.coefficients = coefficients
    
    def _validate_data(self):
        """Ensure all required data is available"""
        if self.df is None or self.coefficients is None or self.media_variables is None or self.media_cost_dict is None:
            raise ValueError("Data, coefficients, variables, and media_cost_dict must be provided")

        # Additional validation
        missing_vars = [var for var in self.coefficients.keys() if var not in self.df.columns]
        if missing_vars:
            raise ValueError(f"Variables {missing_vars} not found in dataframe")
    
    def decomposition(self) -> dict[str, pd.Series]:
        """Calculate the contributions of each variable to the total volume."""
        self._validate_data()
        if self._decomposition_dict is None:
            self._decomposition_dict = {}
            for var in self.coefficients.keys():
                self._decomposition_dict[var] = (self.coefficients[var] * self.df[var])
        return 
    
    def contribution_to_volume(self) -> dict[str, float]:
        """Sum the total decomposition per variable to get the total contribution to volume"""
        if self._contribution_to_volume_dict is None:
            self._contribution_to_volume_dict = {}
            decomposition = self.decomposition
            for key, value in decomposition.items():
                self._contribution_to_volume_dict[key] = value.sum()
        return self._contribution_to_volume_dict
    
    def rel_contribution_to_volume(self) -> dict[str, float]:
        """Calculate relative contribution percentage for media variables"""
        if self._rel_contribution_to_volume_dict is None:
            contribution_dict = self.contribution_to_volume
            
            # Get media contributions (keeping sign to preserve negative contributions)
            media_contributions = {var: contribution_dict[var] for var in self.media_variables}
            
            # Calculate total media contribution
            total_media = sum(media_contributions.values())
            
            if total_media == 0:
                raise ValueError("Total media contribution is 0")
            
            # Calculate relative contributions
            self._rel_contribution_to_volume_dict = {
                var: contrib / total_media 
                for var, contrib in media_contributions.items()
            }
        return self._rel_contribution_to_volume_dict

    def roi(self) -> dict[str, float]:
        """Calculate ROI for each media variable"""
        if self._roi_dict is None:
            self._roi_dict = {}
            contribution_dict = self.contribution_to_volume
            
            for var in self.media_variables:
                if var in self.media_cost_dict:
                    cost = self.media_cost_dict[var]
                    if cost == 0:
                        raise ValueError(f"Media cost for {var} is 0, cannot calculate ROI")
                    self._roi_dict[var] = contribution_dict[var] / cost
                else:
                    raise ValueError(f"Media cost for {var} not found in media_cost_dict")
        return self._roi_dict
