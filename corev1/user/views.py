from corev1.user.models import UserModel
from corev1.serializer.user import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class UserView(APIView):
    @swagger_auto_schema(request_body=UserSerializer, responses={status.HTTP_200_OK: UserSerializer})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Erro ao cadastrar usuário, confira os campos", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=None, responses={status.HTTP_200_OK: UserSerializer})
    def get(self, request, id=None):
        if id:
            usuario = UserModel.objects.get(id=id)
            serializer = UserSerializer(usuario)
            return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

        items = UserModel.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)