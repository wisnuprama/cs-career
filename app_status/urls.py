from django.conf.urls import url
import app_status.views as View

urlpatterns = [
    url(r'private-api/get/status/$', View.get, name='api-status-get'),
    url(r'private-api/get/status/$', View.get, name='api-status-post'),
    url(r'private-api/get/status/$', View.get, name='api-status-delete'),
    # url(r'private-api/get/status/$', View.get, name='status-get'),
]
