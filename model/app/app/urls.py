"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from tastyapp.api import PersonResource, UserResource

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

api = Api(api_name='v1')
api.register(PersonResource())
api.register(UserResource())



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#http://127.0.0.1:8000/api/v1/person/?format=json
#http://127.0.0.1:8000/api/v1/person/2/?username=someuser&api_key=d96845fcaf74bd7ca93b6f5be81dd3a171ed4bda