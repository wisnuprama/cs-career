"""tp_2_ppw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/', include('app_web.urls', namespace='website')),
    url(r'^auth/', include('app_auth.urls', namespace='api-auth')),
    url(r'^api/friend/', include('app_friend.urls', namespace='api-friend')),
    url(r'^api/profile/', include('app_profile.urls', namespace='api-profile')),
    url(r'^api/service/', include('app_service.urls', namespace='api-service')),
    url(r'^api/status/', include('app_status.urls', namespace='api-status')),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
