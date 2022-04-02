from datetime import datetime
from email.policy import default
from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name= models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    organization = models.CharField(max_length=30, blank=False)
    #id = uuid ?

    def __str__(self):
	    return self.first_name

class OrganizationModel(models.Model):
    name = models.CharField(max_length=30, blank=False)
    status = models.BooleanField(blank=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    #id = uuid ?

    def __str__(self):
	    return self.name