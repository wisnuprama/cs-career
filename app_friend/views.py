from django.shortcuts import render
from app_friend import utils as friend_utils
from app_auth import utils as auth_utils
from core.abstract import views as abstractviews


# Create your views here.
def index(request, data):
    npm = request.session['user_login']['npm']
    user = auth_utils.get_or_create_user(npm=npm)
    data['number_of_friend'] = friend_utils.get_number_of_friend(user=user)


def get_all_friend_candidate(request):
    def callback(user):
        mahasiswa_list = friend_utils.get_all_mahasiswa_except(user)
        return {
            'result': mahasiswa_list
        }

    return abstractviews.response(request, method='GET',
                                  auth_type=abstractviews.AUTH_TYPE['LOGIN'], callback=callback)


def post_new_friend(request):

    def callback(user):

        if 'npm' in request.POST:
            npm = request.POST['npm']
            user_new_friend = auth_utils.get_or_create_user(npm=npm)
            friendship = friend_utils.insert_new_friend_to_database(user, user_new_friend)

            result = {
                'result': friend_utils.serialize_friendship(friendship=friendship)
            }

            return result

    return abstractviews.response(request, method='POST', auth_type=abstractviews.AUTH_TYPE['LOGIN'],
                                  callback=callback)

