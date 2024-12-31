from django.db import models

# Create your models here.

class details_table(models.Model):
    user = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    sales = models.FloatField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.CharField(max_length=20, null=True, blank=True)
    cur_date = models.DateField(auto_now_add=True, null=True)
    cur_time = models.TimeField(auto_now=True, null=True)




class register_table(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    # country = models.CharField(max_length=20)
    password = models.CharField(max_length=17)
