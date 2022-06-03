from datetime import datetime
from django.db import models
from user.models import UserModel
import uuid

class FolderModel(models.Model):
    name = models.CharField(max_length=30, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    user_owner  = models.ForeignKey(UserModel, on_delete = models.SET_NULL, null = True)
