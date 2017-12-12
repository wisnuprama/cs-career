from django.conf.urls import url
from .views import get_profile

urlpatterns = [
	url(r'^$', get_profile, name='get-profile'),
]
