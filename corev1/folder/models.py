from ast import Name
from datetime import datetime
from django.db import models
from user.models import UserModel
import uuid

class FolderModel(models.Model):
    name = models.CharField(max_length=30, blank=False)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    user_owner  = models.ForeignKey(UserModel, on_delete = models.SET_NULL, null = True) 

    class Meta:
        verbose_name = "Folder"
