from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import jwt
from django.conf import settings
from datetime import datetime, timedelta

class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.CharField(max_length=30, blank=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=False)
    username = models.CharField(verbose_name='username', max_length=255, unique=True, blank=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        token = jwt.encode(
            {
                'username' : self.username,
                'email' : self.email,
                'exp' : datetime.utcnow() + timedelta(hours=24)
            },
            settings.SECRET_KEY, algorithm='HS256'
        )
        return token
