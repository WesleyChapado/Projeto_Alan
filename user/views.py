from corev1.organization.models import OrganizationModel
from corev1.plan.models import PlanModel
from user.models import UserModel
from user.serializer.user import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserCreate(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer, 
        responses={status.HTTP_200_OK: UserSerializer}
    )

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        plan_id = request.data['plan_id']
        organization_name = request.data['organization']  
        if user_serializer.is_valid():
            try:
                plan = PlanModel.objects.get(id=plan_id) 
            except:
                plan = PlanModel()
                plan.save()

            try:
                organization = OrganizationModel.objects.get(name=organization_name) 
            except OrganizationModel.DoesNotExist:
                organization = OrganizationModel(name=organization_name, plan=plan)
                organization.save()

            user_serializer.save()
            return Response(
                {
                    "message": "Usuário cadastrado com sucesso", 
                    "data": user_serializer.data
                }, 
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Erro ao cadastrar usuário, confira os campos", 
                "data": user_serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

class UserList(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=None, 
        responses={status.HTTP_200_OK: UserSerializer}
    )

    def get(self, request, id=None):
        if id:
            usuario = UserModel.objects.get(id=id)
            serializer = UserSerializer(usuario)
            return Response(
                {
                    "message": "Busca completa", 
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )

        user_list = UserModel.objects.all()
        serializer = UserSerializer(user_list, many=True)
        return Response(
            {
                "message": "Busca completa", 
                "data": serializer.data
            }, 
            status=status.HTTP_200_OK
        )

class LoginView(ObtainAuthToken):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = UserModel.objects.get(email=email, password=password)
        except UserModel.DoesNotExist:
            return Response(
                {"message" : "Email ou senha incorretos"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            Token.objects.get(user=user).delete()
        except:
            pass
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.email
        })
