# Medical Insurance Charges Project

# About this project

The data used in this project is free to use as it is within the public domain. The data can found at the URL below.

https://www.kaggle.com/mirichoi0218/insurance

The dataset reflects variables about medical patients  (gender, smoker status, age , etc) along with the individual medical costs billed by health insurance.

# Project Goals

- Draw insights about what driver medical charges billed by health insurance in the data
- Create a machine learning model that can effectively predict medical charges

# Data Dictionary

age: Age of patient in years

age_s: MinMax scaled (0-1) version of age column

bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

bmi_s: MinMax scaled (0-1) version of bmi column

charges: Individual medical costs billed by health insurance

children: Number of children covered by health insurance / Number of dependents

children_s: MinMax scaled (0-1) version of children column

is_female: Boolean column that represents patient's gender, 0 = male, 1 = female

is_smoker: Boolean column that represents patient's smoker status, 0 = non-smoker, 1 = smoker

region: The beneficiary's residential area in the US, northeast, southeast, southwest, northwest

region_northeast: Boolean column that indicates if patient's address is in the northeast region of the US, 0 = No, 1 = Yes

region_northwest: Boolean column that indicates if patient's address is in the northwast region of the US, 0 = No, 1 = Yes

region_southeast: Boolean column that indicates if patient's address is in the southeast region of the US, 0 = No, 1 = Yes

region_southwest: Boolean column that indicates if patient's address is in the southwest region of the US, 0 = No, 1 = Yes

sex: Patient gender, male or female

smoker: Patient's smoker status, yes = smoker, no = non-smoker

# Project Plan

- __Acquire__
    - Download data as csv from Kaggle
    - Import data into Jupyter Notebook via pandas and save as data frame

- __Prepare__
    - Prepare data as needed for exploration and modeling including but not limited to
        - Dropping unneeded columns
        - Converting all string column values to lower case
        - Updating column names
            - Converting to lower case
            - Change spaces ot underscores
            - Update terms to facilitate understanding
        - Update data types as needed to facilitate expected operations
        - Handle null values via imputing or dropping
        - Convert dates (if any) to datetime format if appropriate for exepected operations
        - Splitting categorical column values into boolean columns 
        - Scaling data where appropriate
        - Splitting data into train, validate and test samples

- __Exploration__
    - Explore each non-target variables relationship with the target variable (charges) via
        - Plotting
        - Hypothesis tests
    - Goal of this section is to identify variables that have drive the target variable (charges) enough to be suitable features for modeling

- __Conclusion__
    - Summarize operations and findings from project

# How to Reproduce
Download data into your working directory. (Link below)

https://www.kaggle.com/mirichoi0218/insurance

Install acquire.py and prepare.py into your working directory.

Run the jupyter notebook.

# Conclusions

- __Acquire__
    - Downloaded data from kaggle as csv
    - Read data into notebook as DF
    
    
- __Prepare__
    - Scaled non-target variable numerical columns
        - age
        - bmi
        - children
    - Created boolean columns for categorical variables
       - sex
       - smoker
       - region
    - Split data in train, validate, test sets
    - No nulls to address
    - Data types were appropriate for the operations I performed
    
    
- __Explore__
    - Through the use of plots and hypothesis tests, the following variables were found to be strong candidates for use as features in modeling to predict charges
        - Age
        - BMI
        - Southeast (Region)
        - Smoker
        
        
- __Modeling__
    - Best Model
        - Type: Generalized Linear Model
        - Features:
            - Age
            - BMI
            - Southeast (Region)
            - Smoker
        - Train (In-Sample) RMSE: 6181.865395
        - Validate (Out-of-Sample) RMSE: 5893.477794
        - Test (Out-of-Sample) RMSE: 5095.42626
