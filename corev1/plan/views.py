from corev1.plan.models import PlanModel
from corev1.serializer.plan import PlanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class PlanView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: PlanSerializer}
    )
    def get(self, request):        
        plan_list = PlanModel.objects.all()
        serializer = PlanSerializer(plan_list, many=True)
        return Response (
            {
                "message" : "Busca completa",
                "data" : serializer.data
            },
            status=status.HTTP_200_OK
        )
