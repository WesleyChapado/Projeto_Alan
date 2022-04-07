def password_validation(password):
    if len(password) < 6:
        return False
    elif not any(i.isupper() for i in password):
        return False
    elif not any(i.islower() for i in password):
        return False
    else:
        return True
