from django.db import models
import uuid

class PlanModel(models.Model):
    FREE = 'free'
    PAID = 'paid'
    PLAN_TYPE = [
        (FREE, 'Free'),
        (PAID, 'Paid')
    ]
    plan_type = models.CharField(max_length=4, choices=PLAN_TYPE, default=FREE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    max_knowledge_base = models.IntegerField(default= '1', blank=True)
    max_megabyte = models.FloatField(default='5', max_length=30, blank=True)
    max_users = models.IntegerField(default= '1', blank=True)
