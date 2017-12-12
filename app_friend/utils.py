from .serializers import FriendshipSerializer
from .models import Friendship
from app_auth import utils as auth_utils


def get_number_of_friend(user):
    return Friendship.objects.filter(user1=user).count()


def serialize_friendship(friendship):
    from core.utils import serialize_instance
    return serialize_instance(FriendshipSerializer, friendship)


def get_user_friends(user):
    return Friendship.objects.filter(user1=user)


def insert_new_friend_to_database(user, user2npm):
    user2 = auth_utils.get_or_create_user(npm=user2npm)
    friendship = Friendship(user1=user, user2=user2)
    friendship.save()
    return friendship


def get_all_mahasiswa_except(user):
    query_user = auth_utils.get_except_user_queryset(npm=user.npm)
    result = [auth_utils.serialize_user(q) for q in query_user]
    return result
