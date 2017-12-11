import app_service.utils as service_utils
from core.abstract import views as abstractviews


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

    return abstractviews.response(request, method='GET', auth_type=abstractviews.AUTH_TYPE['TOKEN'], callback=callback)
