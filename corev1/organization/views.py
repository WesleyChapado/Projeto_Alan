from corev1.organization.models import OrganizationModel
from corev1.serializer.organization import OrganizationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
        
		
class OrganizationView(APIView):
    @swagger_auto_schema(request_body=OrganizationSerializer, responses={status.HTTP_200_OK: OrganizationSerializer})
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Organização cadastrada com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Erro ao cadastrar organização, confira os campos", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=None, responses={status.HTTP_200_OK: OrganizationSerializer})
    def get(self, request, id=None):
        if id:
            organization = OrganizationModel.objects.get(id=id)
            serializer = OrganizationSerializer(organization)
            return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

        organizations = OrganizationModel.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)