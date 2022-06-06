from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from corev1.serializer.folder import FolderSerializer
from corev1.folder.models import FolderModel
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from corev1.folder import validators
from datetime import datetime
from user.models import UserModel

class FolderView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=FolderSerializer, 
        responses={status.HTTP_200_OK: FolderSerializer}
    )

    def post(self, request):
        uuid_usuario = validators.busca_usuario_token(request)
        data = request.data
        data['user_owner'] = uuid_usuario
        folder_serializer = FolderSerializer(data=data)
        if folder_serializer.is_valid():
            folder_serializer.save()
            return Response(
                {
                    "message": "Pasta cadastrada com sucesso", 
                    "data": folder_serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "message": "Erro ao cadastrar pasta, confira os campos", 
                "data": folder_serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: FolderSerializer}
    )

    def get(self, request):
        user_owner = validators.busca_usuario_token(request)
        user = UserModel.objects.get(id=user_owner)
        folder_list = FolderModel.objects.filter(user_owner=user_owner, active=True)
        serializer = FolderSerializer(folder_list, many=True)
        return Response(
            {
                "message": f"Aqui estão todas as pastas do usuário {user.email}", 
                "data": serializer.data
            }, 
            status=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: FolderSerializer}
    )

    def delete(self, request, pk, format=None):
        try:
            user_owner = validators.busca_usuario_token(request)
            folder = FolderModel.objects.get(pk=pk, user_owner=user_owner, active=True)
            folder.deleted = datetime.utcnow()
            folder.active = False
            folder.save()
            serializer = FolderSerializer(folder)
            return Response(
                {
                    "message": "A seguinte pasta foi deletada",
                    "data" : serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    "message": "Id da pasta inválido, tente novamente com um id válido",
                }, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
    
    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: FolderSerializer}
    )

    def put(self, request, pk, format=None):
        try:
            user_owner = validators.busca_usuario_token(request)
            folder = FolderModel.objects.get(pk=pk, user_owner=user_owner)
            folder.updated = datetime.utcnow()
            folder.name = request.data['name']
            folder.save()
            serializer = FolderSerializer(folder)
            return Response(
                {
                    "message": "A seguinte pasta foi atualizada",
                    "data" : serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    "message": "Id da pasta inválido, tente novamente com um id válido",
                }, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
