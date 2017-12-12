from app_profile import utils as profile_utils
from django.http import QueryDict, HttpResponseRedirect
from django.shortcuts import reverse
from core.abstract import views as abstractviews
from app_auth import utils as auth_utils
from .models import Expertise

# Create your views here.
response = {}

def index(request, data):

    data_user = request.session['user_login']

    data['user_riwayat'] = profile_utils.get_query_user_history(data_user['npm'])


def put_profile(request):

    def callback(user):

        PUT = QueryDict(request.body)
        print(PUT)
        print('first_name' in PUT)

        if 'first_name' in PUT:
            user.first_name = PUT.get('first_name')

        if 'last_name' in PUT:
            user.last_name = PUT.get('last_name')

        if 'email' in PUT:
            user.email = PUT.get('email')

        if 'picture_url' in PUT:
            user.picture_url = PUT.get('picture_url')

        if 'id_linkedin' in PUT:
            user.id_linkedin = PUT.get('id_linkedin')

        if 'link_linkedin' in PUT:
            user.link_linkedin = PUT.get('link_linkedin')

        if 'expertise' in PUT and 'level' in PUT:

            expertise = {
                'expertise': PUT.get('expertise'),
                'level': PUT.get('level')
            }

            if 'expertise' in request.session:
                request.session['expertise'].append(expertise)
            else:
                request.session['expertise'] = [expertise]

        user.save()

        request.session['user_login'] = auth_utils.serialize_user(user)

        return request.session['user_login']

    return abstractviews.response(request, method='PUT', auth_type=abstractviews.AUTH_TYPE['LOGIN'], callback=callback)


def save_profile(request):

    if 'expertise' in request.session:
        lst = request.session['expertise']
        for ahli in lst:
            expert = Expertise(user=user, expertise = ahli.get('expertise'), level = ahli.get('level'))
            expert.save()

    return HttpResponseRedirect(reverse('web:dashboard'))
