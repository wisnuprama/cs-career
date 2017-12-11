from django.db import models
from django.contrib.auth.models import User as DjangoUser


# Create your models here.

class User(DjangoUser):
    """
    Description:
    Model for user app

    """

    # basic user
    npm = models.CharField('NPM', primary_key=True, max_length=10, editable=False, unique=True)

    # private
    role = models.CharField('Role', blank=True, max_length=10)
    angkatan = models.PositiveIntegerField('Angkatan')
    is_showing_score = models.BooleanField(default=False)

    # linkedin
    # token_linkedin = models.CharField(blank=True, max_length=1000)

    lastseen_at = models.DateTimeField('Last Seen at', auto_now=True, editable=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True, editable=False)

    def __str__(self):
        return self.npm

    def get_npm(self):
        return self.npm

    #
    # def get_token_linkedin(self):
    #     return self.token_linkedin

    class Meta:
        ordering = ('npm', 'first_name', 'last_name', 'created_at', 'lastseen_at')
