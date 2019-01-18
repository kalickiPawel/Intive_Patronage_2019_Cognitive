import numpy as np

from app.models import Earning
from app.models import Estimate

from sklearn.linear_model import LinearRegression

def run():
    learnWorkedYears = np.asarray(list(Earning.objects.all().values_list('worked_years')))
    learnSalaryBrutto = np.asarray(list(Earning.objects.all().values_list('salary_brutto')))
    workedYears = np.asarray(list(Estimate.objects.all().values_list('pred_worked_years')))
    
    # Create linear regression object
    regr = LinearRegression()
    try: 
        # Train the model using the training sets
        regr.fit(learnWorkedYears.reshape(-1, 1), learnSalaryBrutto.reshape(-1, 1))
    
        # Make predictions using the testing set
        predicted_salary_brutto = regr.predict(workedYears.reshape(-1, 1))

        # Loading data to DataBase
        for index, item in enumerate(Estimate.objects.all()):
            item.pred_salary_brutto=np.around(predicted_salary_brutto[index], decimals=2)
            item.save()
    except:
        print("Estimation Error")
    finally:
        print("Estimation - Done")