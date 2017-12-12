from app_profile import utils as profile_utils
from django.shortcuts import render
from core.abstract import views as abstractviews


# Create your views here.
response = {}

def index(request, data):

    data_user = request.session['user_login']

    data['user_riwayat'] = profile_utils.get_query_user_history(data_user['npm'])


def put_profile(request):

    def callback(user):

        print(request.body['data'])

        result = {
            'username': user.username,
            
        }
        return result

        # status code for delete:
        #   200 if the response include the entity
        #   204 if the response doesnt include the entity
    return abstractviews.response(request, method='PUT', auth_type=abstractviews.AUTH_TYPE['LOGIN'], callback=callback)



def dummy(request):
    return render(request, 'app_profile/edit_profile.html')