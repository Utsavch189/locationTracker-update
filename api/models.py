from django.db import models

# Create your models here.
class Pos(models.Model):
    idd=models.IntegerField(default=0)
    userID=models.CharField(max_length=50,blank=True,null=True)
    latitude=models.CharField(max_length=20,blank=True,null=True)
    longitude=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.userID



class Consumers(models.Model):
    first_name=models.CharField(max_length=50,blank=True,null=True)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.first_name + " "+ self.last_name