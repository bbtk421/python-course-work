from django.db import models
#from . import checkbookApp

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=50, default="")
    LastName = models.CharField(max_length=50, default="")
    StartingBalance = models.DecimalField(max_digits=50, default="", decimal_places=2)

class Transactions(models.Model):
    TransactionDate = models.DateField(max_length=50, default="")
    TransactionType = models.CharField(max_length=50, default="")
    Amount = models.DecimalField(max_digits=50, default="", decimal_places=2)
    Account = models.CharField(max_length=50, default="")
    trans = models.Manager()

