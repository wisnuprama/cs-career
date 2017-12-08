from rest_framework import status
from django.http import HttpResponseBadRequest
# -----
from app_status import utils, forms, serializers
from core.abstract_view import response, RESPONSE_ATTRS


# Create your views here.

def get(request):
    def callback(user):
        query = [utils.serialize_status(st) for st in utils.get_status_queryset(user=user)]
        result = {
            'username': user.username,
            'full_name': user.get_full_name(),
            'role': user.role,
            'result': query,
        }

        return result

    return response(request, method='GET', callback=callback)


def post(request):
    def callback(user):
        form = forms.StatusPostForm(request.POST or None)
        result = None
        if form.is_valid():
            content = request.POST['content']
            status = utils.insert_status_to_database(user=user, content=content)

            result = {
                'username': user.username,
                'full_name': user.get_full_name(),
                'role': user.role,
                'result': utils.serialize_status(status),
            }

        return result

    return response(request, method='POST', callback=callback)


def delete(request, **kwargs):
    if bool(kwargs) and 'pk' in kwargs:
        def callback(user):
            status = utils.delete_status_from_database(user=user, pk=kwargs['pk'])
            result = {
                'username': user.username,
                'full_name': user.get_full_name(),
                'role': user.role,
                'result': utils.serialize_status(status)
            }

            return result

        # status code for delete:
        #   200 if the response include the entity
        #   204 if the response doesnt include the entity
        return response(request, method='DELETE', callback=callback)

    return HttpResponseBadRequest(reason=RESPONSE_ATTRS['error_reason']['no_data'],
                                  content_type=RESPONSE_ATTRS['content_type'])


def put(request, *args, **kwargs):
    if bool(kwargs) and 'pk' in kwargs:
        return

    else:
        pass

    return
