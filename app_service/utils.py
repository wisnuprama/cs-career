import app_auth.csui_helper as CSUIhelper
import app_auth.utils as AuthUtils
from .models import PublicAccess


def get_user_mahasiswa(**kwargs):
    kwargs['role__iexact'] = 'mahasiswa'
    # TODO add data from sso
    return [AuthUtils.serialize_user(user) for user in AuthUtils.get_user_queryset(**kwargs)]


def check_token_existance(**kwargs):
    return PublicAccess.objects.filter(**kwargs).exists()


def get_accessor_or_create(**kwargs):

    if kwargs['token'] and check_token_existance(token=kwargs['token']):
        acc = PublicAccess.objects.get(token=kwargs['token'])

    elif kwargs['email']:
        if check_token_existance(email=kwargs['email']):
            acc = PublicAccess.objects.get(email=kwargs['email'])

        else:
            acc = PublicAccess(email=kwargs['email'])
            acc.save()

    else:
        acc = PublicAccess.objects.filter(**kwargs)

    return acc
