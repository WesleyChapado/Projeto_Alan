from rest_framework import serializers
from corev1.models import UserModel

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		exclude = []