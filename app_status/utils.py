from .models import Status
from django.shortcuts import get_object_or_404
from .serializers import StatusSerializer


def get_status_queryset(user, *args):
    '''
    Get all user's status
    :param user: User user target
    :param kwargs: Order By User Field
    :return: QuerySet of User's Status
    '''
    query = None
    if len(args) == 0:
        query = Status.objects.filter(user=user).order_by(*kwargs)

    else:
        # DEFAULT ORDER
        query = Status.objects.filter(user=user).order_by('-created_at')

    return query


def check_status_existance(user, pk):
    return bool(Status.objects.filter(user=user, pk=pk))


def insert_status_to_database(user, content):
    status = Status(user=user, content=content)
    status.save()
    return status


def delete_status_from_database(user, pk):
    status = get_object_or_404(Status, user=user, pk=pk)
    status.delete()
    return status


def serialize_status(status):
    from core.utils import serialize_instance
    return serialize_instance(StatusSerializer, status)
