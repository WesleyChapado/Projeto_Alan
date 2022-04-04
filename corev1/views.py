from rest_framework import viewsets
from corev1.models import OrganizationModel, UserModel
from corev1.serializer import UserSerializer, OrganizationSerializer

class UserView(viewsets.ModelViewSet):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer

class OrganizationView(viewsets.ModelViewSet):
	queryset = OrganizationModel.objects.all()
	serializer_class = OrganizationSerializer
