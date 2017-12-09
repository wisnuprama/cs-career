from django.db import models
from app_auth.models import User


# Create your models here.


class Friendship(models.Model):
    # connect between two people
    user1 = models.ForeignKey(to=User, related_name='user1')
    user2 = models.ForeignKey(to=User, related_name='user2')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.user, self.friend)

    class Meta:
        ordering = ('created_at',)
