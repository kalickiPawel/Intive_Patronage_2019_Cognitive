from django.db import models

# Create your models here.
class Earning(models.Model):
    
    salary_brutto = models.FloatField()
    worked_years = models.FloatField()

    def __str__(self):
        return f'{self.salary_brutto} {self.worked_years}'

class Estimate(models.Model):
    pred_worked_years = models.FloatField()
    pred_salary_brutto = models.FloatField()

    def __str__(self):
        return f'{self.pred_salary_brutto} {self.pred_worked_years}'