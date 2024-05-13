from django.db import models

class register(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

    class Meta:
        db_table = "register"
