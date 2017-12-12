from app_profile import utils as profile_utils
from django.shortcuts import render
import app_auth.utils as auth_utils

# Create your views here.
response = {}

def get_profile(request, data):

    data_user = request.session['user_login']

    data['user_riwayat'] = profile_utils.get_query_user_history(data_user['npm'])
    response['name'] = request.session['name']
    response['npm'] = data_user['npm']
    response['keahlian'] = data.session['keahlian']
    response['email'] = data.session['email']
    response['account'] = data.session['account']
    response['baru'] = True
    # return request

    #if() 
    #kalo belom login linkedin, bakal keluar silakan isi profil dahulu
    if response['baru'] == True :
        response['name'] = 'kosong'
        response['npm'] = user_login.npm()
        response['keahlian'] = 'kosong'
        response['email'] = 'kosong'
        response['account'] = 'kosong'
        html = 'app_profile/profile.html'
        return render(data, html, response)

    else:    
        html = 'app_profile/profile.html'
        return render(data, html, response)


