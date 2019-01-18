#! /usr/bin/env python
#-*- coding: utf-8 -*-

"""
    Created by: Paweł Kalicki
    Date: 27.12.2018
    Last Update: 18.01.2019
    Version: v2
"""

import numpy as np
import matplotlib.pyplot as plt

from load_data import load_data
from estimate_earning import estimate_earning

if __name__ == "__main__":
    
    try: 
        data = load_data()
    except Exception as ex:
        print("Error using the function")
        print(ex)
    
    worked_years = data[2]

    try:
        predicted_salary_brutto = estimate_earning(data)
    except Exception as ex:
        print("Error using the function")
        print(ex)
    
    # drawing plot
    #plt.scatter(workedYears, predicted_salary_brutto, color='red', marker="x")
    plt.plot(worked_years, predicted_salary_brutto, color='blue', linewidth=3, marker="o", markerfacecolor="red")
    # I drew the line because Linear Regression plot is linear

    plt.show()

    # usually value of money is rounded up
    print(np.around(predicted_salary_brutto, decimals=2))
