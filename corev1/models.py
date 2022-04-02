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