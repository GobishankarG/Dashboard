from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=17)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    def __str__(self):
        return self.email