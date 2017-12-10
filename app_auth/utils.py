from django.contrib.auth.models import Group, Permission
from django.contrib.sessions.models import Session
from .models import User
from .serializers import UserSerializer


class SSOException(Exception):
    def __init__(self):
        super().__init__(self, "Unidentified Username or Password")


SSO_GROUP_NAME = 'UserSSO'


def get_permission_for_sso_user():
    list_permission_name = ['Can add user', 'Can change user', 'Can delete user', 'Can add friendship',
                            'Can change friendship', 'Can delete friendship', 'Can add expertise',
                            'Can change expertise', 'Can delete expertise', 'Can add comment', 'Can change comment',
                            'Can delete comment', 'Can add status', 'Can change status', 'Can delete status']

    result = []
    for name in list_permission_name:
        result.append(Permission.objects.get(name=name))

    return result


def get_or_create_sso_group():
    if not Group.objects.filter(name=SSO_GROUP_NAME).exists():
        perm = get_permission_for_sso_user()
        group = Group(name=SSO_GROUP_NAME)
        group.permissions.set(perm)
        group.save()
    else:
        group = Group.objects.get(name=SSO_GROUP_NAME)
    return group


def check_user_existence(**kwargs):
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
    if check_user_existence(npm=npm):
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
        group = get_or_create_sso_group()
        user.groups.add(group)
        user.save()

    return user


def get_user_queryset(**kwargs):
    return User.objects.filter(**kwargs)


def check_user_session_existence(request):
    print('haha')
    sess_key = request.COOKIES['sessionid']
    return Session.objects.filter(session_key=sess_key).exists()


def set_user_session_data(request):
    pass


def get_user_session(request):
    sess_key = request.COOKIES['sessionid']
    session = Session.objects.get(session_key=sess_key)
    return session


def serialize_user(user):
    from core.utils import serialize_instance
    return serialize_instance(UserSerializer, user)
