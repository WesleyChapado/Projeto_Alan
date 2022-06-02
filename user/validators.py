def password_validation(password):
    '''
        Verificia se a senha possui ao menos 6 caracteres, uma letra mauiúscula e uma letra minúscula
    '''
    if len(password) < 6:
        return False
    elif not any(i.isupper() for i in password):
        return False
    elif not any(i.islower() for i in password):
        return False
    else:
        return True
