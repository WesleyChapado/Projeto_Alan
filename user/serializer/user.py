from rest_framework import serializers
from user.models import UserModel
from user.validators import *
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(validators=[UniqueValidator(queryset=UserModel.objects.all(), message="Este email já está cadastrado")])	
	
	class Meta:
		model = UserModel
		fields = ['id', 'email', 'first_name', 'last_name', 'organization', 'password']

	def validate(self, data):
		if not password_validation(data['password']):
			raise serializers.ValidationError({'password':"Digite uma senha com no mínimo 6 caracteres, pelo menos uma letra maiúscula e uma minúscula"})
		return data