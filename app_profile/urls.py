from django.conf.urls import url

from .views import put_profile, save_profile

urlpatterns = [
	url(r'^put/$', put_profile, name='put-profile'),
	url(r'^save/$', save_profile, name='save-profile')
]
