from django.db import models

class myClass(models.Model):
    faculty_name=models.CharField(max_length=50)
    date=models.DateField()
    start=models.TimeField()
    end=models.TimeField()
    course=models.CharField(max_length=50)
    description=models.TextField(max_length=500)