from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    Currency_CHOICES = (
        ('BDT', 'BDT'),
        ('INR', 'INR'),
        ('USD', 'USD'),
    )
    currency = models.CharField(max_length=30,choices=Currency_CHOICES)


class Source(models.Model):
    Source_CHOICES = (
        ('Salary', 'Salary'),
        ('Business', 'Business'),
        ('Others', 'Others'),
    )
    Source = models.CharField(max_length=30,choices=Source_CHOICES)


class Income(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    Source = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='Source')
    Currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='Currency')
    IncomeDate = models.DateField()

    def __str__(self):
        return self.username
