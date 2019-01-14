from django.db import models

# Create your models here.
class EstimateEarning(models.Model):
    
    salary_brutto = models.FloatField()
    worked_years = models.FloatField()

    def __str__(self):
        return f'{self.salary_brutto} {self.worked_years}'