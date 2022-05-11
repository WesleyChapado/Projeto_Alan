from rest_framework import serializers
from corev1.plan.models import PlanModel

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanModel
        fields = ('__all__')