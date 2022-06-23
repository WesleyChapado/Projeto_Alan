from django.db import models
from datetime import datetime
from user.models import UserModel
import uuid

class DialogModel(models.Model):
    question = models.TextField(max_length=None, blank=False)
    answer = models.TextField(max_length=None, blank=False)
    file = models.CharField(max_length=250, blank=False)
    user_owner  = models.ForeignKey(UserModel, on_delete = models.SET_NULL , null=True)
    dialog_id = models.UUIDField(editable=False)
    answer_id = models.CharField(max_length=250, blank=False)
    folder_name = models.CharField(max_length=250, blank=False)
    created = models.DateTimeField(default=datetime.now, blank=True, editable=False)

    class Meta:
        verbose_name = "Dialog"