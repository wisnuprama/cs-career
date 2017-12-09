from .serializers import FriendshipSerializer


def serialize_friendship(friendship):
    from core.utils import serialize_instance
    return serialize_instance(FriendshipSerializer, friendship)
