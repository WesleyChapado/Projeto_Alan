from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from corev1.dialog.models import DialogModel
from corev1.serializer.document import DocumentSerializer
from corev1.serializer.dialog import DialogSerializer
from corev1.document.models import DocumentModel
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from user import validators
from datetime import datetime
from user.models import UserModel
from corev1.document.pdf_manager import PdfManager

class DocumentView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=DocumentSerializer, 
        responses={status.HTTP_200_OK: DocumentSerializer}
    )

    def post(self, request, format=None):
        uuid_usuario = validators.busca_usuario_token(request)
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid() and validators.verifica_titularidade_da_pasta(request.data['folder'], uuid_usuario):
            document = serializer.save(
                user_owner=UserModel.objects.get(id=uuid_usuario),
                file_size=request.data['file'].size
            )
            document_save = PdfManager(document)
            document_save.save()
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

class SearchPdfView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        uuid_usuario = validators.busca_usuario_token(request)
        if validators.verifica_titularidade_da_pasta(request.data['folder_id'], uuid_usuario):
            dialog_id = PdfManager.search(
                question=request.data['question'], 
                kb_uuid=request.data['folder_id'], 
                uuid_usuario = uuid_usuario
            )
            answer = DialogModel.objects.filter(dialog_id=dialog_id)
            serializer = DialogSerializer(answer, many=True)
            return Response(
                {
                    'message': 'Aqui estão os arquivos que correspondem a busca',
                    'data': serializer.data
                },
                status.HTTP_200_OK
            )
        return Response(
                {
                    'message': 'Esta pasta pertence a outro usuário'
                },
                status.HTTP_400_BAD_REQUEST
            )
