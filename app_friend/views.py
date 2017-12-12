from django.shortcuts import render
from app_friend import utils as friend_utils
from app_auth import utils as auth_utils
from core.abstract import views

# Create your views here.
def index(request, data):
    npm = request.session['user_login']['npm']
    user = auth_utils.get_or_create_user(npm=npm)
    data['number_of_friend'] = friend_utils.get_number_of_friend(user=user)

def get_all_friend_candidate(request):

	def callback(user):
		mahasiswalist = friend_utils.get_all_mahasiswa_except(user)
		return {
			'result': mahasiswalist
		}

	return views.response(request, method='GET', auth_type=0, callback=callback)
