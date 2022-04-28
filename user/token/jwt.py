from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from user.models import UserModel

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed('Este token não é válido')

        token = auth_token[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')

            email = payload['email']
            user = UserModel.objects.get(email=email)
            return (user, token)

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('Seu token expirou, faça login novamente!')

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed('Token inválido!')
        
        except UserModel.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed('Usuário não encontrado')
