from rest_framework import serializers
from corev1.models import UserModel, OrganizationModel

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		exclude = []

class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrganizationModel
		exclude = []