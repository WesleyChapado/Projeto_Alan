from rest_framework import serializers
<<<<<<< HEAD
from corev1.models import UserModel, OrganizationModel
=======
from corev1.models import UserModel
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
<<<<<<< HEAD
		exclude = []

class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrganizationModel
=======
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5
		exclude = []