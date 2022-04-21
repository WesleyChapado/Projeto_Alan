from rest_framework import serializers
from corev1.organization.models import OrganizationModel

class OrganizationSerializer(serializers.ModelSerializer):	
	class Meta:
		model = OrganizationModel
		fields = ('__all__')