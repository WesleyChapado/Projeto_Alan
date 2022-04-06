from rest_framework import viewsets
from corev1.models import OrganizationModel, UserModel
from corev1.serializer import UserSerializer, OrganizationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# class UserView(viewsets.ModelViewSet):
# 	queryset = UserModel.objects.all()
# 	serializer_class = UserSerializer

# class OrganizationView(viewsets.ModelViewSet):
# 	queryset = OrganizationModel.objects.all()
# 	serializer_class = OrganizationSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Erro ao cadastrar usuário, confira os campos", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            usuario = UserModel.objects.get(id=id)
            serializer = UserSerializer(usuario)
            return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

        items = UserModel.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)
		
class OrganizationView(APIView):
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Organização cadastrada com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Erro ao cadastrar organização, confira os campos", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            organization = OrganizationModel.objects.get(id=id)
            serializer = OrganizationSerializer(organization)
            return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

        organizations = OrganizationModel.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)
