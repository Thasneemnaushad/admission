from django.db import models

# Create your models here.
class assessment(models.Model):
    assessment_name=models.CharField(max_length=50,null=True,blank=True)
    date=models.CharField(max_length=10,null=True,blank=True)
    subject=models.CharField(max_length=30,null=True,blank=True)
    faculty=models.CharField(max_length=30,null=True,blank=True)
    class mete:
        db_table='assessment'
