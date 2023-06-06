from django.db import models

# Create your models here.
class Trabajador(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    age = models.IntegerField()
    start_date = models.DateField()
    salary = models.FloatField(default=0)