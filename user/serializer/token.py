from rest_framework import serializers
from user.models import UserModel

class LoginSerializer(serializers.ModelSerializer):	
	class Meta:
		model = UserModel
		fields = ['email', 'token']

    