from datetime import timedelta
import datetime
import email
from rest_framework.response import Response
from rest_framework.views import APIView
from alan.settings import OAUTH2_PROVIDER
from oauth2_provider.models import AccessToken, Application
from user.models import UserModel
from rest_framework import status

class TokenView(APIView):
    def post(self, request):
        user = UserModel.objects.get(email=request.data['email'])
        expire_seconds = OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
        scopes = ' '.join(OAUTH2_PROVIDER['SCOPES'].keys())
        application = Application.objects.get(name="ApplicationName")
        expires = datetime.now() + timedelta(seconds=expire_seconds)
        access_token = AccessToken.objects.create(
                        user=user,
                        application=application,
                        token=random_token_generator(request),
                        expires=expires,
                        scope=scopes)

        token = {
                        'access_token': access_token.token,
                        'token_type': 'Bearer',
                        'expires_in': expire_seconds,
                        'scope': scopes}

        return Response(token, status=status.HTTP_200_OK)

