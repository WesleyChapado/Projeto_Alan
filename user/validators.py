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
