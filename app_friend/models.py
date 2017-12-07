from django.db import models
from app_auth.models import User


# Create your models here.


class Friend(models.Model):
    # connect between two people
    user = models.ForeignKey(to=User)
    friend = models.ForeignKey(to=User, related_name='user_friend')

    is_accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.user, self.friend)

    class Meta:
        ordering = ('created_at',)
