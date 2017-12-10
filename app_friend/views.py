from django.shortcuts import render
from app_friend import utils as friend_utils
from app_auth import utils as auth_utils


# Create your views here.
def index(request, data):
    npm = request.session['user_login']['npm']
    user = auth_utils.get_user_or_create(npm=npm)
    data['number_of_friend'] = friend_utils.get_number_of_friend(user=user)
