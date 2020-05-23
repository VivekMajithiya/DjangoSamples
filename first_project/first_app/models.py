from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.top_name

class Webpages(models.Model):
    top_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,unique=True)
    url=models.URLField()

    def __str__(self):
        return self.name

class AccessTracker(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
