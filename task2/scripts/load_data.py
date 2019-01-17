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
                                earnings = Earning.objects.all().delete()
                                for row in reader:
                                        try:
                                                salary = float(row['salaryBrutto'])
                                        except:
                                                pred_years = float(row['workedYears'])
                                                Estimate.objects.create(pred_worked_years=pred_years, pred_salary_brutto=0)
                                        try:
                                                years = float(row['workedYears'])
                                        except:
                                                break
                                        Earning.objects.create(salary_brutto=salary, worked_years=years)
                        os.unlink(FILENAME)
                else:
                        print("The file was not found or added to the database")
                
        except Exception as ex:
                print(ex)
                print("Adding items to database failed")
        finally:
                print("The process of adding elements has been completed")
