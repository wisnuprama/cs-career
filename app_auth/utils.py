from .models import User
from .serializers import UserSerializer


class SSOException(Exception):

    def __init__(self):
        super().__init__(self, "Unidentified Username or Password")


def check_user_existance(**kwargs):
    '''
    Check if user has existed or not.
    :param npm: identity number
    :return: boolean True if user is exist, False otherwise
    '''
    if len(kwargs) == 0:
        return False

    return bool(User.objects.filter(**kwargs))


def get_user_or_create(npm, **kwargs):
    '''
    Get user by NPM if user has existed, otherwise create new one and return it.
    The **kwargs argument is only for create, for get only using npm.
    :param npm: identity number
    :return: User
    '''
    if check_user_existance(npm=npm):
        user = User.objects.get(npm=npm)

    else:
        user = User(npm=npm)

        if kwargs:
            if kwargs['username']:
                user.username = kwargs['username']
            if kwargs['angkatan']:
                user.angkatan = kwargs['angkatan']
            if kwargs['role']:
                user.role = kwargs['role']

        user.save()

    return user


def get_user_queryset(**kwargs):
    return User.objects.filter(**kwargs)


def get_user_session_data(request, key):
    sess = None

    if key in request.session:
        sess = request.session[key]

    return sess


def set_user_session_data(request):
    pass


def serialize_user(user):
    from core.utils import serialize_instance
    return serialize_instance(UserSerializer, user)
