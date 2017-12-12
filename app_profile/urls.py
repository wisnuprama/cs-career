from django.conf.urls import url
from .views import get_profile, put_profile

urlpatterns = [
	url(r'^$', get_profile, name='get-profile'),
	url(r'^$', put_profile, name='put-profile'),

]


