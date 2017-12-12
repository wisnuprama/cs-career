from django.conf.urls import url

from .views import put_profile, dummy

urlpatterns = [
    url(r'^dummy/$', dummy),
    url(r'^put/$', put_profile, name='put-profile'),
]
