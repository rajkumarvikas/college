from django.db import models
from users.models.registration import User_Model

# Create your models here.
class Sem_sixth(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    semester=models.CharField(default='6',max_length=1,editable=False)
    paper_title=models.CharField(max_length=50)
    obtain_marks=models.IntegerField()