from corev1.organization.models import OrganizationModel
from corev1.serializer.organization import OrganizationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated      
		
class OrganizationView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=None, responses={status.HTTP_200_OK: OrganizationSerializer})
    def get(self, request, id=None):
        if id:
            organization = OrganizationModel.objects.get(id=id)
            serializer = OrganizationSerializer(organization)
            return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)

        organizations = OrganizationModel.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response({"message": "Busca completa", "data": serializer.data}, status=status.HTTP_200_OK)