from django.db import models


# Create your models here.

def user_directory_img_path(instance, filename):
    return 'image/user/{0}/profile/{1}'.format(instance.username, filename)


class User(models.Model):
    """
    Description:
    Model for user app

    """

    # basic user
    npm = models.CharField('NPM', primary_key=True, max_length=10, editable=False, unique=True)
    username = models.CharField('Username', unique=True, max_length=128)

    # private
    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)
    email = models.EmailField('Email', blank=True, unique=True)
    role = models.CharField('Role', blank=True, max_length=10)
    angkatan = models.PositiveIntegerField('Angkatan')
    is_showing_score = models.BooleanField(default=False)

    # linkedin
    # token_linkedin = models.CharField(blank=True, max_length=1000)

    lastseen_at = models.DateTimeField('Last Seen at', auto_now=True, editable=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True, editable=False)

    def __str__(self):
        return self.npm

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_npm(self):
        return self.npm

    def getUsername(self):
        return self.username

    #
    # def get_token_linkedin(self):
    #     return self.token_linkedin

    class Meta:
        ordering = ('npm', 'first_name', 'last_name', 'created_at', 'lastseen_at')
