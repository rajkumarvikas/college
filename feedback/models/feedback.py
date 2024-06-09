from django.db import models

class Model_Feedback(models.Model):
    query_type=models.CharField(max_length=50)
    query_title=models.CharField(max_length=50)
    justify=models.CharField(max_length=50)
    