from rest_framework import viewsets
from corev1.models import UserModel
from corev1.serializer import UserSerializer

class UserView(viewsets.ModelViewSet):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer