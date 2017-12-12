from django.conf.urls import url
from app_friend import views

urlpatterns = [
	url(r'^get-friend-candidate/$', views.get_all_friend_candidate, name='get-all-friend-candidate'),
]