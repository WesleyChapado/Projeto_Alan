from django.db import models
import uuid
from authemail.models import EmailUserManager, EmailAbstractUser
from django.contrib.auth import get_user_model

class UserModel(EmailAbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name= models.CharField(max_length=30, blank=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=False)
    organization = models.CharField(max_length=30, blank=False)
    objects = EmailUserManager()

