from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class UserProfile(AbstractUser):
      phone=models.CharField(max_length=10,blank=True)
      gender=models.CharField(max_length=15,blank=True)
      hobby=models.CharField(max_length=255,blank=True)
      birth_date = models.DateField(null=True, blank=True)

      objects = UserManager()







# def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

# objects = UserManager()

# def __str__(self):
#         return self.username