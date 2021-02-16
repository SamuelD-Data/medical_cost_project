import pandas as pd

def get_med_insurance_data():
    """
    No arguments needed. Run function to acquire raw medical insurance charge data.
    """

    # acquiring data from local csv downloaded from Kaggle
    df = pd.read_csv('insurance.csv')

    # returning df
    return df