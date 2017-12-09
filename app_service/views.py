from django.shortcuts import render
from core.abstract_view import response, AUTH_TYPE
import app_service.utils as service_utils


# Create your views here.

def get(request):
    def callback(accesss):

        query = {}

        if 'npm' in request.GET:
            query['npm'] = request.GET['npm']

        if 'username' in request.GET:
            query['username'] = request.GET['username']

        if 'angkatan' in request.GET:
            query['angkatan'] = request.GET['angkatan']

        if 'first_name' in request.GET:
            query['first_name__icontains'] = request.GET['first_name']

        if 'last_name' in request.GET:
            query['last_name__icontains'] = request.GET['last_name']

        result = {
            'result': service_utils.get_user_mahasiswa(**query)
        }

        return result

    return response(request, method='GET', auth_type=AUTH_TYPE['TOKEN'], callback=callback)
