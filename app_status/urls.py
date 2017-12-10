from django.conf.urls import url
import app_status.views as views

urlpatterns = [
    url(r'get/$', views.get, name='get-status'),
    url(r'post/$', views.post, name='post-status'),
    url(r'delete/$', views.delete, name='delete-status'),
    # url(r'private-api/get/status/$', View.get, name='status-get'),
]
