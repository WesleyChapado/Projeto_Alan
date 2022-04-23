from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# from authemail.models import EmailUserManager, EmailAbstractUser

# class UserModel(EmailAbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=30, blank=False)
#     last_name= models.CharField(max_length=30, blank=False)
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=False)
#     organization = models.CharField(max_length=30, blank=False)
#     objects = EmailUserManager()

class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.CharField(max_length=30, blank=False)

