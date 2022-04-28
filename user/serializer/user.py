from rest_framework import serializers
from user.models import UserModel
from user.validators import *

class UserSerializer(serializers.ModelSerializer):	
	class Meta:
		model = UserModel
		fields = ['id','username', 'email', 'first_name', 'last_name', 'organization', 'password']

	def validate(self, data):
		if not password_validation(data['password']):
			raise serializers.ValidationError({'password':"Digite uma senha com no mínimo 6 caracteres, pelo menos uma letra maiúscula e uma minúscula"})
		return data