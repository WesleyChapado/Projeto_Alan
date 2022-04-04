from rest_framework import viewsets
<<<<<<< HEAD
from corev1.models import OrganizationModel, UserModel
from corev1.serializer import UserSerializer, OrganizationSerializer

class UserView(viewsets.ModelViewSet):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer

class OrganizationView(viewsets.ModelViewSet):
	queryset = OrganizationModel.objects.all()
	serializer_class = OrganizationSerializer
=======
from corev1.models import UserModel
from corev1.serializer import UserSerializer

class UserView(viewsets.ModelViewSet):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5
