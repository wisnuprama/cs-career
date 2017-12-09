from django.conf.urls import url
import app_auth.views as View
import app_auth.views as Views


urlpatterns = [
    url(r'^login/$', View.auth_login, name='login'),
    url(r'^logout/$', View.auth_logout, name='logout'),
]