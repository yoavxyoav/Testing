
import numpy as np

def add_cum_calc(user_revenue_dataset: pd.DataFrame, cal_type: str):
    if cal_type == 'sum':
        grouped = user_revenue_dataset.groupby('user_id').cumsum()
        concatenated = pd.concat((user_revenue_dataset, grouped), axis=1)
        concatenated.columns = concatenated.columns.to_list()[:-1] + ['cum_sum']
        return concatenated

    elif cal_type == 'avg':
        grouped = user_revenue_dataset.groupby('user_id')['revenues'].expanding().mean().reset_index(0)
        concatenated = pd.concat((user_revenue_dataset, grouped), axis=1)
        concatenated.columns = concatenated.columns.to_list()[:-1] + ['cum_mean']
        concatenated = concatenated.loc[:,~concatenated.columns.duplicated()]

        return concatenated

    elif cal_type == 'max':
        grouped = user_revenue_dataset.groupby('user_id').cummax()
        concatenated = pd.concat((user_revenue_dataset, grouped), axis=1)
        concatenated.columns = concatenated.columns.to_list()[:-1] + ['cum_max']
        return concatenated

    elif cal_type == 'min':
        grouped = user_revenue_dataset.groupby('user_id').cummin()
        concatenated = pd.concat((user_revenue_dataset, grouped), axis=1)
        concatenated.columns = concatenated.columns.to_list()[:-1] + ['cum_min']
        return concatenated

    else:
        raise Exception('Please choose a valid calculation.')
