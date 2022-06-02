from rest_framework.authtoken.models import Token
from user.models import UserModel

def busca_usuario_token(request):
    '''
        Retorna o uuid do usuário que está usando o token
    '''
    token = request.headers['Authorization'][6:]
    token_usuario = Token.objects.get(key=token)
    usuario = UserModel.objects.get(email=token_usuario.user)
    return usuario.id
    
