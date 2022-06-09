from cgitb import text
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from corev1.serializer.document import DocumentSerializer
from corev1.document.models import DocumentModel
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from user import validators
from datetime import datetime
from user.models import UserModel
from corev1.document import pdf_manager

class DocumentView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=DocumentSerializer, 
        responses={status.HTTP_200_OK: DocumentSerializer}
    )

    def post(self, request, format=None):
        uuid_usuario = validators.busca_usuario_token(request)
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user_owner=UserModel.objects.get(id=uuid_usuario),
                file_size=request.data['file'].size
            )
            return Response(
                {
                    "message": "Documento cadastrado com sucesso", 
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Erro ao cadastrar documento, confira os campos",
                "data": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: DocumentSerializer}
    )

    def get(self, request):
        user_owner = validators.busca_usuario_token(request)
        user = UserModel.objects.get(id=user_owner)
        list = DocumentModel.objects.filter(user_owner=user_owner, active=True)
        serializer = DocumentSerializer(list, many=True)
        return Response(
            {
                "message": f"Aqui estão todos os documentos do usuário {user.email}", 
                "data": serializer.data
            }, 
            status=status.HTTP_200_OK
        )
    
    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: DocumentSerializer}
    )

    def delete(self, request, uuid, format=None):
        try:
            user_owner = validators.busca_usuario_token(request)
            document = DocumentModel.objects.get(uuid=uuid, user_owner=user_owner, active=True)
            document.deleted = datetime.utcnow()
            document.active = False
            document.save()
            serializer = DocumentSerializer(document)
            return Response(
                {
                    "message": "O seguinte documento foi deletado",
                    "data" : serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        except DocumentModel.DoesNotExist:
            return Response(
                {
                    "message": "Erro ao deletar documento, uuid inválido ou documento não pertence a este usuário",
                }, 
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: DocumentSerializer}
    )

    def put(self, request, uuid, format=None):
        try:
            user_owner = validators.busca_usuario_token(request)
            document = DocumentModel.objects.get(uuid=uuid, user_owner=user_owner)
            serializer = DocumentSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save(
                    file_size=request.data['file'].size,
                    updated=datetime.utcnow()
                )          
                return Response(
                    {
                        "message": "O seguinte documento foi atualizado",
                        "data" : serializer.data
                    }, 
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "Erro ao atualizar documento, confira os campos", 
                    "data": serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except DocumentModel.DoesNotExist:
            return Response(
            {
                "message": "Erro ao atualizar documento, uuid inválido ou documento não pertence a este usuário"
            }, 
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

class OpenPdfView(APIView):
    def get(self, request, uuid):
        try:
            text = pdf_manager.read_using_document_uuid(uuid)
            return Response(
                {
                    'message': '=)',
                    'data': text
                }
            )
        except:
            return Response(
                {
                    'message': 'Informe um uui válido para a busca'
                },
                status.HTTP_400_BAD_REQUEST
            )