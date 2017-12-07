from .models import User
import secrets
import string


class SSOException(Exception):

    def __init__(self):
        super().__init__(self, "Unidentified Username or Password")


def generate_token():
    BYTES = 32
    return secrets.token_hex(BYTES)


def check_user_existance(npm):
    '''
    Check if user has existed or not.
    :param npm: identity number
    :return: boolean True if user is exist, False otherwise
    '''
    return bool(User.objects.filter(npm=npm))


def get_user_or_create(npm):
    '''
    Get user by NPM if user has existed, otherwise create new one and return it
    :param npm: identity number
    :return: User
    '''
    if check_user_existance(npm):
        user = User.objects.get(npm=npm)

    else:
        user = User(npm=npm)
        user.save()

    return user


def get_user_session_data(request, key):
    sess = None

    if key in request.session:
        sess = request.session[key]

    return sess


def set_user_session_data(request):
    pass
