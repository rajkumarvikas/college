from django.db import models
from users.models.registration import User_Model

# Create your models here.
class Sem_sixth(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    semester=models.CharField(default=6,max_length=1,editable=False)
    project_name=models.IntegerField()
    seminar_presentation=models.IntegerField()
    viva_voce=models.IntegerField()
    total_obtain=models.IntegerField()