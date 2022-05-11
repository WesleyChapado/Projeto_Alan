from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
import pytz
import datetime
from rest_framework.authtoken.models import Token

class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Token inválido')    

        utc_now = datetime.datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created <utc_now - datetime.timedelta(hours=24):
            raise AuthenticationFailed('Token expirado')

        return token.user, token