import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import sklearn

def prep_med_insurance_data(df):
    """
    Accepts raw df of medical insurance data. Return train, validate, and test samples, fully prepped.
    """

    # creating dummy columns
    df_dummies = pd.get_dummies(df, columns = ['sex', 'region' , 'smoker'], prefix = ['is','region', 'smoker'])

    # renaming smoker column to match other binary column
    df_dummies.rename(columns = {'smoker_yes' : 'is_smoker'}, inplace=True)

    # resetting df indices otherwise merge causes extra rows to be created
    df_dummies.reset_index(inplace = True)
    df.reset_index(inplace = True)

    # merging dummy df with main df
    df = df.merge(df_dummies, how = 'inner')

    # dropping these columns since their information is stored in counterpart column since they are binary values in this case
    # ie. only male and female in data, if patient not female, must be male
    # ie. if patient is a smoker, they must not be a non-smoker
    # also dropping index here since passing drop argument to reset_index function also causes new row creation
    df = df.drop(columns = ['is_male', 'smoker_no', 'index'])

    # splitting data
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    # creating scaler object
    scaler = sklearn.preprocessing.MinMaxScaler()

    # columns to scale
    col_to_scale = ['age', 'bmi', 'children']
    col_scaled_names = ['age_s', 'bmi_s', 'children_s']

    # creating columns for scaled values
    train['age_s'], train['bmi_s'], train['children_s'] = 0,0,0
    validate['age_s'], validate['bmi_s'], validate['children_s'] = 0,0,0
    test['age_s'], test['bmi_s'], test['children_s'] = 0,0,0

    # fitting scaler to train column and scaling after
    train[col_scaled_names] = scaler.fit_transform(train[col_to_scale])

    # scaling data in validate and test dataframes
    validate[col_scaled_names] = scaler.transform(validate[col_to_scale])
    test[col_scaled_names] = scaler.transform(test[col_to_scale])

    # removing charges column from df and saving as variable
    charges_train, charges_val, charges_test = [train.pop('charges'), validate.pop('charges'), test.pop('charges')]
        
    # adding back charges columns to end of DF
    train['charges'] = charges_train
    validate['charges'] = charges_val
    test['charges'] = charges_test

    # returning DFs
    return train, validate, test