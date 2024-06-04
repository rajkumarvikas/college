from django.db import models
from users.models.registration import User_Model

    
class Document_Url(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    photo_url=models.CharField(max_length=500)
    signatue_url=models.CharField(max_length=500)
    adhar_url=models.CharField(max_length=500)
    tenth_url=models.CharField(max_length=500)
    twelth_url=models.CharField(max_length=500)
    