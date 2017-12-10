from django.core import paginator
from rest_framework import status, pagination, generics
from django.http import HttpResponseBadRequest, QueryDict
from django.shortcuts import reverse
# -----
from app_status import utils, forms, serializers, models
from core.abstract_view import response, RESPONSE_ATTRS, AUTH_TYPE
import app_auth.utils as auth_utils


# Create your views here.
def index(request, data):
    npm = request.session['user_login']['npm']
    user = auth_utils.get_user_or_create(npm=npm)
    data['number_of_status'] = utils.get_number_of_status(user=user)
    data['status_form'] = forms.StatusPostForm

    if data['number_of_status'] > 0:
        # start from page one
        data['latest_status'] = utils.get_latest_status(user=user)
        data['query_of_status'] = utils.get_status_queryset(user=user)[:11]


def get(request):
    def callback(user):
        # start from page 2
        query = utils.get_status_queryset(user=user)

        page = int(request.GET.get('page', 1))
        if query.count() > 1:
            int(request.GET.get('page', 2))

        paginate = paginator.Paginator(query, 10)

        try:
            query = paginate.page(page)
        except paginator.PageNotAnInteger:
            query = paginate.page(1)
        except paginator.EmptyPage:
            query = paginate.page(paginator.num_pages)

        BASE_URL = reverse('api-status:get-status')
        next_url = ''
        if query.has_next():
            next_url = BASE_URL + '?page={}'.format(query.next_page_number())

        previous_url = ''
        if query.has_previous():
            previous_url = BASE_URL + '?page={}'.format(query.previous_page_number())

        result = {
            'username': user.username,
            'result': [utils.serialize_status(st) for st in query],
            'next_page': next_url,
            'previous_page': previous_url,
        }

        return result

    return response(request, method='GET', auth_type=AUTH_TYPE['LOGIN'], callback=callback)


def post(request):
    def callback(user):
        form = forms.StatusPostForm(request.POST or None)
        result = None
        if form.is_valid():
            content = request.POST['content']
            status = utils.insert_status_to_database(user=user, content=content)

            result = {
                'username': user.username,
                'result': utils.serialize_status(status),
            }

        return result

    return response(request, method='POST', auth_type=AUTH_TYPE['LOGIN'], callback=callback)


def delete(request):

    def callback(user):
        delete = QueryDict(request.body)

        if 'id' not in delete:
            return None

        status = utils.delete_status_from_database(user=user, pk=delete.get('id'))
        result = {
            'username': user.username,
            'result': utils.serialize_status(status)
        }
        return result

        # status code for delete:
        #   200 if the response include the entity
        #   204 if the response doesnt include the entity
    return response(request, method='DELETE', auth_type=AUTH_TYPE['LOGIN'], callback=callback)


def put(request, *args, **kwargs):
    if bool(kwargs) and 'pk' in kwargs:
        return

    else:
        pass

    return


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StatusView(generics.ListAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    pagination_class = StandardResultsSetPagination
