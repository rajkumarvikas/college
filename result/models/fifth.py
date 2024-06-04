from django.db import models
from users.models.registration import User_Model

# Create your models here.
class Sem_fifth(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    semester=models.CharField(default=5,max_length=1,editable=False)
    paper_code=models.CharField(max_length=7,default="BCA-")
    paper_title=models.CharField(max_length=50)
    internal_marks=models.IntegerField()
    external_marks=models.IntegerField()
    obtain_marks=models.IntegerField()