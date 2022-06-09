from datetime import datetime
from django.db import models
from user.models import UserModel
import uuid

class DocumentModel(models.Model):
    name = models.CharField(max_length=30, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=datetime.now, blank=True, editable=False)
    file_size = models.CharField(max_length=30, blank=True)
    file = models.FileField(upload_to='pdf/', blank=False)
    deleted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    user_owner  = models.ForeignKey(UserModel, on_delete = models.SET_NULL, null = True)
