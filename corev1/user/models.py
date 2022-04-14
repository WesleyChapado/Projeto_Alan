from datetime import datetime
from django.db import models
import uuid

class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name= models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    organization = models.CharField(max_length=30, blank=False)

    def __str__(self):
	    return self.first_name