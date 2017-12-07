from django.shortcuts import render, get_object_or_404
from rest_framework import status
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, \
    Http404, HttpResponseBadRequest, HttpResponseForbidden
# -----
from tp_2_ppw import strings
from app_status import utils, forms
from app_auth import utils as AuthUtils

RESPONSE_ATTRS = {
    'content_type': 'application/json',
    'error_reason': {
        'no_access': 'ERROR: You don\'t have an access',
        'no_method': 'ERROR: Unexpected method',
        'no_data': 'ERROR: No data posted'
    },

}


# Create your views here.
def response(request, method, callback, status_code=status.HTTP_200_OK, *args, **kwargs):
    '''
    This function is used for basic method to return json response. To use this function
    you need to create callback function to use this function, include the callback function in the parameter.
    The callback function must return tuplpe consists of response in dict/list format
    and json safe parameter (for more information please read documentation for JsonResponse Safe Parameter).

    :param request: HttpRequest
    :param method: String REST method
    :param callback: Function callback
    :param status_code: int for JsonResponse status
    :param args:
    :param kwargs:
    :return: JsonResponse response
    '''

    if request.method == method:

        if 'user_npm' in request.session:

            user = AuthUtils.get_user_or_create(npm=request.session['user_npm'])
            result = callback(user=user)

            if result:
                return JsonResponse(data=result, status=status_code,
                                    content_type=RESPONSE_ATTRS['content_type'])

        else:
            return HttpResponseForbidden(reason=RESPONSE_ATTRS['error_reason']['no_access'],
                                         content_type=RESPONSE_ATTRS['content_type'])

    return HttpResponseBadRequest(reason=RESPONSE_ATTRS['error_reason']['no_method'],
                                  content_type=RESPONSE_ATTRS['content_type'])


def get(request):
    def callback(user):
        query = utils.get_status_queryset(user=user)
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
            status = Status(user=user, content=content)
            status.save()

            result = {
                'username': user.username,
                'full_name': user.get_full_name(),
                'role': user.role,
                'result': {
                    'status': {
                        'content': status.content,
                        'likes': status.likes,
                        'created_at': status.created_at,
                    }
                }
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
                'result': {
                    'status': {
                        'content': status.content,
                        'likes': status.likes,
                        'created_at': status.created_at,
                    }
                }
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
