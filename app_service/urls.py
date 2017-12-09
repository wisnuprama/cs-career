from django.conf.urls import url
import app_service.views as Views


urlpatterns = [
    url(r'^mahasiswa/$', Views.get, name='get-data-mahasiswa'),
]