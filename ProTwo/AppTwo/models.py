from django.db import models

# Create your models here.
class UserInfo(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    User_Email=models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name
