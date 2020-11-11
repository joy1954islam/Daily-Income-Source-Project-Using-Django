from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Income(models.Model):
    Currency_CHOICES = (
        ('BDT', 'BDT'),
        ('INR', 'INR'),
        ('USD', 'USD'),
    )
    Source_CHOICES = (
        ('Salary', 'Salary'),
        ('Business', 'Business'),
        ('Others', 'Others'),
    )
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(blank=True,null=True)
    Source = models.CharField(max_length=30,choices=Source_CHOICES)
    currency = models.CharField(max_length=30, choices=Currency_CHOICES)
    IncomeDate = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('Income', kwargs={'pk': self.pk})