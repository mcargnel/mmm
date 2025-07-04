import pandas as pd

class Contributions:
    def __init__(self, df: pd.DataFrame, coefficients: dict[str, float]):
        self.df = df
        self.coefficients = coefficients
    
    def _validate_data(self):
        """Ensure all required data is available"""
        if self.df is None or self.coefficients is None:
            raise ValueError("Data, coefficients must be provided")

        # Additional validation
        missing_vars = [var for var in self.coefficients.keys() if var not in self.df.columns]
        if missing_vars:
            raise ValueError(f"Variables {missing_vars} not found in dataframe")
    
    def decomposition(self) -> dict[str, pd.Series]:
        """Calculate the contributions of each variable to the total volume."""
        self._validate_data()
        
        decomposition_dict = {}
        for var in self.coefficients.keys():
            decomposition_dict[var] = (self.coefficients[var] * self.df[var])
        return decomposition_dict
    
    def contribution_to_volume(self, decomposition) -> dict[str, float]:
        """Sum the total decomposition per variable to get the total contribution to volume"""
        contribution_to_volume_dict = {}
        
        for key, value in decomposition.items():
            contribution_to_volume_dict[key] = value.sum()
        return contribution_to_volume_dict
    
    def rel_contribution_to_volume(self,media_variables:list ,contribution_dict: dict[str,float]) -> dict[str, float]:
        
        """Calculate relative contribution percentage for media variables"""
            # Get media contributions (keeping sign to preserve negative contributions)
        
        rel_contribution_to_volume_dict = {}
        
        media_contributions = {var: contribution_dict[var] for var in media_variables}
            
        # Calculate total media contribution
        total_media = sum(media_contributions.values())
            
        if total_media == 0:
            raise ValueError("Total media contribution is 0")
            
            # Calculate relative contributions
        rel_contribution_to_volume_dict = {
            var: contrib / total_media 
            for var, contrib in media_contributions.items()
        }
        return rel_contribution_to_volume_dict

    def roi(self, contribution_dict:dict[str, float],  media_variables: list[str], media_cost_dict: dict[str, float]) -> dict[str, float]:
 
        """Calculate ROI for each media variable"""
        
        roi_dict = {}
            
        for var in media_variables:
            if var in media_cost_dict:
                cost = media_cost_dict[var]
                if cost == 0:
                    raise ValueError(f"Media cost for {var} is 0, cannot calculate ROI")
                roi_dict[var] = contribution_dict[var] / cost
            else:
                raise ValueError(f"Media cost for {var} not found in media_cost_dict")
        return roi_dict
