import re
import app_service.utils as service_utils

RE_PUBLIC_TOKEN = re.compile(r'^PUBLIC_TOKEN')


def check_token_existance_in_header(request):
    return True if get_access_token_from_headers(request) else False


def get_access_token_from_headers(request):
    for (header, value) in request.META.items():
        if RE_PUBLIC_TOKEN.match(header):
            return header, value

    return None


def check_request_authorization(request):
    header, token = get_access_token_from_headers(request)
    print(header, value)
    if service_utils.check_token_existance(token=token):
        return service_utils.get_accessor_or_create(token=token)

    return None
