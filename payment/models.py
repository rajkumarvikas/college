from django.db import models
from users.models.registration import User_Model

# Create your models here.
class Payement(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    pay=models.BooleanField(default=False)