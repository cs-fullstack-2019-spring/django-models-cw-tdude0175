from django.db import models
# added classes and used [CharField] in {models} for easy to read
class Dogs(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)

# used numbers for accountNumber and balance to make it more understandable

class Account(models.Model):
    userName = models.CharField(max_length=100)
    realName = models.CharField(max_length=100)
    accountNumber = models.IntegerField(default=0)
    balace = models.DecimalField(decimal_places=2,max_digits=7)