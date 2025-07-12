import matplotlib.pyplot as plt
import warnings

class Vizualization:
    """
    This class is used to visualize the results of the MMM.
    In particular, it is used to compute: contributions, roi, decomp, due to volume, marginal effects, and contribution roi matrix.
    
    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the data.
    """
    def __init__(self):
        pass

    def plot_contributions(self, total_contrib: dict) -> tuple[plt.Figure, plt.Axes]:
        """
        Plot the contributions of the media variables to the total volume.
        
        Parameters
        ----------
        total_contrib : dict
            Dictionary with variable names as keys and contribution values as values
            
        Returns
        -------
        tuple[plt.Figure, plt.Axes]
            The figure and axes objects
        """
        # Create a copy to avoid modifying the original dictionary
        contrib_copy = total_contrib.copy()
        
        # validate that values are positive and take absolute values if needed
        for key, value in contrib_copy.items():
            if value < 0:
                warnings.warn(f"Variable '{key}' has a negative contribution ({value:.3f}). Taking absolute value.")
                contrib_copy[key] = abs(value)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.pie(contrib_copy.values(), labels=list(contrib_copy.keys()), autopct='%1.0f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Contribution to Volume')
        
        return fig, ax
    
    
    def plot_roi(self, roi_dict: dict) -> tuple[plt.Figure, plt.Axes]:
        """
        Plot the ROI for each media variable.
        
        Parameters
        ----------
        roi_dict : dict
            Dictionary with variable names as keys and ROI values as values
            
        Returns
        -------
        tuple[plt.Figure, plt.Axes]
            The figure and axes objects
        """
        fig, ax = plt.subplots(figsize=(10, 5))

        bars = ax.bar(roi_dict.keys(), roi_dict.values())
        ax.set_xlabel('Variables')
        ax.set_ylabel('ROI')
        ax.set_title('Return on Investment by Variable')

        # Add labels in the center of each bar
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                        xytext=(0, 0),  # No offset, center of the bar
                        textcoords="offset points",
                        ha='center', va='center')

        return fig, ax

    def weekly_decomp(self, decomp_dict: dict, dates: list) -> tuple[plt.Figure, plt.Axes]:
        """
        Plot the weekly decomposition of contributions using a stacked area chart.
        
        Parameters
        ----------
        decomp_dict : dict
            Dictionary with variable names as keys and pd.Series (weekly contributions) as values
        dates : list
            List of dates for x-axis
            
        Returns
        -------
        tuple[plt.Figure, plt.Axes]
            The figure and axes objects
        """

        # Sort the keys of decomp_dict (excluding 'week') by the highest sum of their series
        decomp_keys = [k for k in decomp_dict.keys()]
        sorted_keys = sorted(decomp_keys, key=lambda k: decomp_dict[k].sum(), reverse=True)
        sorted_decomp_dict = {k: decomp_dict[k] for k in sorted_keys}
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Get the dates for x-axis
        x_axis = dates
        
        # Prepare data for stackplot
        # We need to separate positive and negative contributions
        positive_contributions = {}
        negative_contributions = {}
        
        for var, series in sorted_decomp_dict.items():
            pos_series = series.where(series >= 0, 0)
            neg_series = series.where(series < 0, 0)
            
            if pos_series.sum() > 0:
                positive_contributions[var] = pos_series
            if neg_series.sum() < 0:
                negative_contributions[var] = neg_series
        
        # Plot positive contributions
        if positive_contributions:

            pos_labels = list(positive_contributions.keys())
            pos_values = [positive_contributions[var].values for var in pos_labels]
            ax.stackplot(x_axis, *pos_values, labels=pos_labels, alpha=0.8)
        
        # Plot negative contributions
        if negative_contributions:
            warnings.warn(f"Negative contributions found in weekly decomposition: {negative_contributions.keys()}")
            neg_labels = list(negative_contributions.keys())
            neg_values = [negative_contributions[var].values for var in neg_labels]
            ax.stackplot(x_axis, *neg_values, labels=neg_labels, alpha=0.8)

        ax.set_xlabel('Time Period')
        ax.set_ylabel('Contribution')
        ax.set_title('Weekly Decomposition of Contributions')
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        
        ax.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        return fig, ax
    
    def due_to_volume(self, decomp_dict: dict, week: int) -> tuple[plt.Figure, plt.Axes]:
        """
        Plot the due to volume of the media variables. Due tue plots shows the sum of the contributions of the variables from one period to another. The goal is to understand how variables contribute to the difference in volume between periods.
        
        Parameters
        ----------
        decomp_dict : dict
            Dictionary with variable names as keys and pd.Series (weekly contributions) as values
        dates : list
            List of dates for x-axis
        
        Returns
        -------
        tuple[plt.Figure, plt.Axes]
            The figure and axes objects
        """

        total_list_1 = sum(series.iloc[:week].sum() for series in decomp_dict.values())
        contrib_list_2 = {var: series.iloc[week:].sum() for var, series in decomp_dict.items()}

        dict_test = {'0-'+str(week): total_list_1}
        for var, series in contrib_list_2.items():
            dict_test[var] = series

        # Sort dict_test by values
        dict_test = dict(sorted(dict_test.items(), key=lambda item: item[1], reverse=True))

        dict_test['total'] = sum(dict_test.values())

        fig, ax = plt.subplots(figsize=(8, 4))

        # Convert dict values and keys to lists for indexing
        values = list(dict_test.values())
        labels = list(dict_test.keys())

        # Calculate cumulative values for the waterfall
        cumulative = [values[0]]
        for v in values[1:-1]:
            cumulative.append(cumulative[-1] + v)

        # Bar positions and colors
        bar_positions = range(len(labels))
        bar_colors = ['blue'] + ['green' if v > 0 else 'red' for v in values[1:]]

        # Plot bars
        ax.bar(bar_positions[0], values[0], color=bar_colors[0])
        for i in range(1, len(values)-1):
            ax.bar(bar_positions[i], values[i], bottom=cumulative[i-1], color=bar_colors[i])
        # Last bar (End) starts at y=0
        ax.bar(bar_positions[-1], values[-1], color=bar_colors[-1])

        # Add labels
        ax.set_xticks(bar_positions)
        ax.set_xticklabels(labels)
        ax.set_title('Simple Waterfall Chart')
        ax.set_ylabel('Value')
        ax.set_ylim(0, max(values)*1.1)

        return fig, ax


    def plot_contribution_roi_matrix(self, roi_dict: dict, rel_contrib_to_vol_dict: dict, total_execution_dict: dict) -> tuple[plt.Figure, plt.Axes]:
        """
        Plot contribution-ROI matrix. This plot has the contribution to volume on the x-axis and the ROI on the y-axis. With a bouble size as the total execution of each variable.
        
        Parameters
        ----------
        roi_dict : dict
            Dictionary with variable names as keys and ROI values as values
        rel_contrib_to_vol_dict : dict
            Dictionary with variable names as keys and relative contribution to volume values as values
        total_execution_dict : dict
            Dictionary with variable names as keys and total execution values as values

        Returns
        -------
        tuple[plt.Figure, plt.Axes]
            The figure and axes objects
        """

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.scatter(rel_contrib_to_vol_dict.values(), roi_dict.values(), s=total_execution_dict.values(), alpha=0.7)

        for var in rel_contrib_to_vol_dict.keys():
            ax.annotate(
                var,
                (rel_contrib_to_vol_dict[var], roi_dict[var])
            )
        
        avg_contribution = sum(rel_contrib_to_vol_dict.values()) / len(rel_contrib_to_vol_dict)
        avg_roi = sum(roi_dict.values()) / len(roi_dict)

        ax.axhline(avg_roi, color='red', linestyle='--', label='Average ROI')
        ax.axvline(avg_contribution, color='blue', linestyle='--', label='Average Contribution to Volume')
        
        ax.set_xlabel('Contribution to Volume')
        ax.set_ylabel('ROI')
        ax.set_title('Contribution-ROI Matrix')
        ax.set_xlim(min(rel_contrib_to_vol_dict.values())*0.95, max(rel_contrib_to_vol_dict.values())*1.05)
        ax.set_ylim(min(roi_dict.values())*0.95, max(roi_dict.values())*1.05)
        ax.legend()

        return fig, ax

    def plot_marginal_effects(self) -> tuple[plt.Figure, plt.Axes]:

        pass



