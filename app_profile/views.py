from django.shortcuts import render

from app_profile import utils as profile_utils

# Create your views here.
response = {}


def index(request, data):
    data_user = request.session['user_login']
    data['user_riwayat'] = profile_utils.get_query_user_history(data_user['npm'])


def put_profile(request):
    pass


def dummy(request):
    return render(request, 'app_profile/edit_profile.html')
