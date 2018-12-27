"""
    Created by: Paweł Kalicki
    Date: 27.12.2018
"""

#! /usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

FILENAME = "salary.csv"

def LoadData():
    """
        This function read the csv file
        and looks for a place to divide the data set.
        Return the tuple with <numpy.ndarray> objects:
            - worked years
            - salary brutto
            - worked years to prediction
    """
    df = pd.read_csv(FILENAME)  # declared DataFrame container
    
    dataIndexesToComplete = df[df['salaryBrutto'].isnull()].index.tolist() # empty value - indexes
    dataIndexesToComplete.extend(df[df['salaryBrutto']==' '].index.tolist()) # NaN value - indexes
    dataIndexesToComplete = list(set(dataIndexesToComplete)) # if NaN is first sort indexes
    
    stopTrainDataIndex = dataIndexesToComplete[0] # end training data and start testing(predicting) data
    
    # training set
    X = trainDataWorkedYears = df["workedYears"][0:stopTrainDataIndex].astype(float)
    Y = trainDataSalaryBrutto = df["salaryBrutto"][0:stopTrainDataIndex].astype(float)
    
    # testing set
    xPred = predDataWorkedYears = df["workedYears"][stopTrainDataIndex:].astype(float)

    return(X.values, Y.values, xPred.values)

def EstimateEarning(data):
    """
        This function gets the data
        and perform Linear Regression process
        Return the <numpy.ndarray> object:
            - predicted salary brutto
    """
    learnWorkedYears = data[0]
    learnSalaryBrutto = data[1]
    workedYears = data[2]
    
    # Create linear regression object
    regr = LinearRegression()
    
    # Train the model using the training sets
    regr.fit(learnWorkedYears.reshape(-1, 1), learnSalaryBrutto.reshape(-1, 1))
    
    # Make predictions using the testing set
    predicted_salary_brutto = regr.predict(workedYears.reshape(-1, 1))
    
    return(predicted_salary_brutto)

if __name__ == "__main__":

    data = LoadData()
    
    workedYears = data[2]
    predicted_salary_brutto = EstimateEarning(data)
    
    # drawing plot
    #plt.scatter(workedYears, predicted_salary_brutto, color='red', marker="x")
    plt.plot(workedYears, predicted_salary_brutto, color='blue', linewidth=3, marker="o", markerfacecolor="red")
    # I drew the line because Linear Regression plot is linear

    plt.show()

    # usually value of money is rounded up
    print(np.around(predicted_salary_brutto, decimals=2))
