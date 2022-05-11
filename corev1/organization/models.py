from datetime import datetime
from django.db import models
from corev1.plan.models import PlanModel
import uuid

class OrganizationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank=False)
    status = models.BooleanField(blank=False, default=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    plan = models.ForeignKey(PlanModel, on_delete = models.SET_NULL, null = True)
