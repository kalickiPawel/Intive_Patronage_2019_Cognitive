import csv
import os

from app.models import Earning
from app.models import Estimate

FILENAME = './salary.csv'

def run():
        try:
                if os.path.isfile(FILENAME):
                        with open(FILENAME) as csvfile:
                                reader = csv.DictReader(csvfile)
                                earning = Earning.objects.all().delete()
                                estimate = Estimate.objects.all().delete()

                                salary = []
                                pred_years = []
                                years = []

                                for row in reader:
                                        try:
                                                salary.append(float(row['salaryBrutto']))
                                        except:
                                                pred_years.append(float(row['workedYears']))
                                        try:
                                                years.append(float(row['workedYears']))
                                        except:
                                                break
                                for i in range(len(pred_years)):
                                        Estimate.objects.create(pred_worked_years=pred_years[i], pred_salary_brutto=0)
                                for j in range(len(salary)):
                                        Earning.objects.create(salary_brutto=salary[j], worked_years=years[j])
                        os.unlink(FILENAME)
                else:
                        print("The file was not found or added to the database")
                
        except Exception as ex:
                print(ex)
                print("Adding items to database failed")
        finally:
                print("The process of adding elements has been completed")
