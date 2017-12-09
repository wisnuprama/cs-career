from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, \
    Http404, HttpResponseBadRequest, HttpResponseForbidden
import app_auth.utils as auth_utils
import app_service.utils as service_utils

RESPONSE_ATTRS = {
    'content_type': 'application/json',
    'error_reason': {
        'no_access': 'ERROR: You don\'t have an access',
        'no_method': 'ERROR: Unexpected method',
        'no_data': 'ERROR: No data posted'
    },

}

AUTH_TYPE = {
    'LOGIN': 0,
    'TOKEN': 1
}


def response(request, method, auth_type, callback, status_code=status.HTTP_200_OK, *args, **kwargs):
    '''
    This function is used for basic method to return json response. To use this function
    you need to create callback function to use this function, include the callback function in the parameter.
    The callback function must return tuplpe consists of response in dict/list format
    and json safe parameter (for more information please read documentation for JsonResponse Safe Parameter).

    :param request: HttpRequest
    :param method: String REST method
    :param auth_type: int login type
    :param callback: Function callback
    :param status_code: int for JsonResponse status
    :param args:
    :param kwargs:
    :return: JsonResponse response
    '''

    if request.method == method:

        result = None

        if auth_type == 0 and 'user_npm' in request.session:
            user = auth_utils.get_user_or_create(npm=request.session['user_npm'])
            result = callback(user)

        elif auth_type == 1 and 'public_token' in request.GET:
            token = request.GET['public_token']
            access = service_utils.check_token_existance(token=token)

            if access:
                acc = service_utils.get_accessor_or_create(token=token)
                result = callback(acc)

        # return the json response
        if result:
            return JsonResponse(data=result, status=status_code,
                                content_type=RESPONSE_ATTRS['content_type'])

        return HttpResponseForbidden(reason=RESPONSE_ATTRS['error_reason']['no_access'],
                                     content_type=RESPONSE_ATTRS['content_type'])

    return HttpResponseBadRequest(reason=RESPONSE_ATTRS['error_reason']['no_method'],
                                  content_type=RESPONSE_ATTRS['content_type'])
