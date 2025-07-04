import pandas as pd
import numpy as np
from src.utils import geometric_adstock, saturation, mean_scaling


def gen_data(beta_1 =3.0, beta_2 = 2.0, beta_event = 1.5, intercept = 2.0):

    seed = 73815

    np.random.seed(seed)

    # Option 2: Use generator consistently (recommended)
    rng = np.random.default_rng(seed=seed)

    # data range
    min_date = pd.to_datetime('1997-01-01')
    max_date = pd.to_datetime('1999-12-31')

    df = pd.DataFrame(
        data = {"date_week" : pd.date_range(start=min_date, end=max_date, freq="W-MON")}
    )

    df['day_of_year'] = df['date_week'].dt.dayofyear

    n = df.shape[0]

    x1 = rng.uniform(low=0.0, high=1.0, size=n)
    df["x1"] = np.where(x1 > 0.9, x1, x1 / 2)

    x2 = rng.uniform(low=0.0, high=1.0, size=n)
    df["x2"] = np.where(x2 > 0.8, x2, 0)

    df['x1_sat_media_cost'] = rng.normal(loc = 1, scale = 0.5, size = n)
    df['x2_sat_media_cost'] = rng.normal(loc = 1, scale = 0.5, size = n)

    # alpha parameters were randomly selected

    df['x1_adstocked'] = geometric_adstock(x1, 0.4)
    df['x2_adstocked'] = geometric_adstock(x2, 0.2)

    df['x1_sat'] = saturation(df['x1_adstocked'], 2)
    df['x2_sat'] = saturation(df['x2_adstocked'], 5)

    df['trend'] = (np.linspace(start=0.0, stop=50, num=n) + 10) ** (1/4) -1

    df["cs"] = -np.sin(2 * 2 * np.pi * df["day_of_year"] / 365.5)
    df["cc"] = np.cos(1 * 2 * np.pi * df["day_of_year"] / 365.5)
    df["seasonality"] = 0.5 * (df["cs"] + df["cc"])

    df['event_1'] = (df['date_week'] == "1997-06-09").astype(float)

    df['intercept'] = intercept
    df['epsilon'] = rng.normal(size=n)

    betas = [beta_1, beta_2]
    df['y'] = (
        df['intercept'] + 
        df['trend'] + 
        df['seasonality'] + 
        beta_event * df['event_1'] + 
        beta_1 * df['x1_sat'] + 
        beta_2 * df['x2_sat'] + 
        df['epsilon']
    )

    return df



if __name__ == "__main__":
    print("Script is runnning directly")
    result = gen_data()
    print(result)

    
