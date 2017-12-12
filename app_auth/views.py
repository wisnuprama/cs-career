from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponseBadRequest
from django.urls import reverse
from django.contrib import messages
# -----
import app_auth.csui_helper as CSUIHelper
from .forms import LoginForm
import app_auth.utils as AuthUtils


def auth_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        __USERNAME__ = request.POST['username']
        __PASSWORD__ = request.POST['password']

        try:
            access_token = CSUIHelper.get_access_token(__USERNAME__, __PASSWORD__)
        except AuthUtils.SSOException as e:
            print(e)
            access_token = None

        if access_token:
            verified_user = CSUIHelper.verify_user(access_token=access_token)

            if __USERNAME__ == verified_user['username']:
                npm = verified_user['identity_number']
                role = verified_user['role']

                user_data = CSUIHelper.get_user_data(access_token=access_token, id=npm)
                user = AuthUtils.get_or_create_user(npm=npm,
                                                    username=__USERNAME__,
                                                    role=role,
                                                    angkatan=user_data['program'][0]['angkatan']
                                                    )

                # set user session
                request.session['user_login'] = AuthUtils.serialize_user(user=user)
                request.session['access_token'] = access_token

            else:
                return HttpResponseForbidden(reason='Error: Unexpected behavior')

        else:
            messages.error(request, 'Login: Unidentified username or password')

    else:
        return HttpResponseBadRequest(reason='Error: Unexpected method')

    # TODO FINISH WITH REVERSE URL
    return HttpResponseRedirect(reverse('web:dashboard'))


def auth_logout(request):
    if request.method == 'GET':
        request.session.flush()
    else:
        return HttpResponseBadRequest(reason='Error: Unexpected method')

    # TODO FINISH WITH REVERSE URL
    return HttpResponseRedirect(reverse('web:index'))
