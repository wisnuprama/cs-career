from django.conf.urls import url
import app_status.views as View

urlpatterns = [
    url(r'get/$', View.get, name='get-status'),
    url(r'post/$', View.get, name='post-status'),
    url(r'delete/$', View.get, name='delete-status'),
    # url(r'private-api/get/status/$', View.get, name='status-get'),
]
