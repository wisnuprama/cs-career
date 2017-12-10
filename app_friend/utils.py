from .serializers import FriendshipSerializer
from .models import Friendship


def get_number_of_friend(user):
    return Friendship.objects.filter(user1=user).count()


def serialize_friendship(friendship):
    from core.utils import serialize_instance
    return serialize_instance(FriendshipSerializer, friendship)
