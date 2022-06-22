from rest_framework.authtoken.models import Token
from corev1.folder.models import FolderModel
from user.models import UserModel

def password_validation(password):
    '''
        Verifica se a senha possui ao menos 6 caracteres, uma letra maiúscula e uma letra minúscula
    '''
    if len(password) < 6:
        return False
    elif not any(i.isupper() for i in password):
        return False
    elif not any(i.islower() for i in password):
        return False
    else:
        return True

def busca_usuario_token(request):
    '''
        Retorna o uuid do usuário que está usando o token
    '''
    token = request.headers['Authorization'][6:]
    token_usuario = Token.objects.get(key=token)
    usuario = UserModel.objects.get(email=token_usuario.user)
    return usuario.id

def verifica_titularidade_da_pasta(folder_uuid, user_uuid):
    '''
        Verifica se a pasta pertence ao usuário
    '''
    try:
        folder = FolderModel.objects.get(uuid=folder_uuid)
        user = UserModel.objects.get(id=folder.user_owner.id)
        if user.id == user_uuid:
            return True
        return False
    except:
        return False
    