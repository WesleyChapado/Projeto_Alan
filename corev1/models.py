<<<<<<< HEAD
from datetime import datetime
from email.policy import default
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

class OrganizationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank=False)
    status = models.BooleanField(blank=False)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
	    return self.name
=======
from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    #id = uuid ?

    def __str__(self):
	    return self.first_name
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5
