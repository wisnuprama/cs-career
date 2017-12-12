from django.conf.urls import url
from .views import put_profile

urlpatterns = [
	url(r'^$', put_profile, name='put-profile'),

]


