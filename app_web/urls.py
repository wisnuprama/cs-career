from django.conf.urls import url
import app_web.views as Views

urlpatterns = [
    url(r'^$', Views.index, name='index'),
    url(r'^dashboard/$', Views.index_dashboard, name='dashboard'),
]