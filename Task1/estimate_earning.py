
from sklearn.linear_model import LinearRegression

def estimate_earning(data):
    """
        This function gets the data
        and perform Linear Regression process
        Return the <numpy.ndarray> object:
            - predicted salary brutto
    """
    learn_worked_years = data[0]
    learn_salary_brutto = data[1]
    worked_years = data[2]
    
    # Create linear regression object
    regr = LinearRegression()
    try:
        # Train the model using the training sets
        regr.fit(learn_worked_years.reshape(-1, 1), learn_salary_brutto.reshape(-1, 1))
        
        # Make predictions using the testing set
        predicted_salary_brutto = regr.predict(worked_years.reshape(-1, 1))
    except:
        print("Error Training the model")
    
    return(predicted_salary_brutto)