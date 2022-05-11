from corev1.organization.models import OrganizationModel
from user.models import UserModel
from user.serializer.token import LoginSerializer
from user.serializer.user import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from user.token.jwt import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserCreate(APIView):
    @swagger_auto_schema(request_body=UserSerializer, responses={status.HTTP_200_OK: UserSerializer})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        organization = OrganizationModel(name=request.data['organization'])    
        if serializer.is_valid():
            organization.save()
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"message": "Erro ao cadastrar usuário, confira os campos", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=None, responses={status.HTTP_200_OK: UserSerializer})
    def get(self, request, id=None):
        if id:
            usuario = UserModel.objects.get(id=id)
            serializer = UserSerializer(usuario)
            return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

        items = UserModel.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = UserModel.objects.get(email=email)
            if user.password == password:
                serializer = LoginSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message":"Senha incorreta, tente novamente"}, status=status.HTTP_401_UNAUTHORIZED)
        except UserModel.DoesNotExist as no_user:
            return Response({"message":"Email não encontrado, tente novamente"}, status=status.HTTP_401_UNAUTHORIZED)

