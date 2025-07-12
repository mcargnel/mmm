import pandas as pd

from src.data_generation import gen_data
from src.linear_regression import LinearRegression
from src.contributions import Contributions


print("Generating Data")
df = gen_data()

indep_vars = ['x1_sat', 'x2_sat', 'trend',
'seasonality', 'event_1']

lm = LinearRegression(df, 'y',indep_vars)

results = lm.fit()

lm.summary()

coefs_lm = lm.get_coefficients()

contrib_lm = Contributions(df, coefs_lm)

decomp_lm = contrib_lm.decomposition()

contrib_to_vol_lm = contrib_lm.contribution_to_volume(decomp_lm)

media_vars = ['x1_sat', 'x2_sat']

rel_contribution_to_volume_lm = contrib_lm.rel_contribution_to_volume(media_vars, contrib_to_vol_lm)



media_cost_dict = {
'x1_sat' : df['x1_sat_media_cost'].sum(),
'x2_sat' : df['x2_sat_media_cost'].sum()
}


roi_lm = contrib_lm.roi(contrib_to_vol_lm,media_vars, media_cost_dict)
print(roi_lm)