import pandas as pd

FILENAME = "salary.csv"

def load_data():
    """
        This function read the csv file
        and looks for a place to divide the data set.
        Return the tuple with <numpy.ndarray> objects:
            - worked years
            - salary brutto
            - worked years to prediction
    """
    df = pd.read_csv(FILENAME)  # declared DataFrame container
    
    data_indexes_to_complete = df[df['salaryBrutto'].isnull()].index.tolist() # empty value - indexes
    data_indexes_to_complete.extend(df[df['salaryBrutto']==' '].index.tolist()) # NaN value - indexes
    data_indexes_to_complete = list(set(data_indexes_to_complete)) # if NaN is first sort indexes
    
    stop_train_data_index = data_indexes_to_complete[0] # end training data and start testing(predicting) data
    
    # training set
    x = train_data_worked_years = df["workedYears"][0:stop_train_data_index].astype(float)
    y = train_data_salary_brutto = df["salaryBrutto"][0:stop_train_data_index].astype(float)
    
    # testing set
    x_pred = pred_data_worked_years = df["workedYears"][stop_train_data_index:].astype(float)

    return(x.values, y.values, x_pred.values)