"""ikazi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from  django.contrib.auth.models  import  Group
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header  =  "IkokaziKenya"
admin.site.site_title  =  "IkokaziKenyae"
admin.site.index_title  =  "IkokaziKenya"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('api/',include('jobs.urls')),
    path('api/', include('blogs.urls')),
    path('api/',include('message.urls')),
    path('docs/', include_docs_urls(title = 'IKOKAZI Kenya',authentication_classes=(),)),
    path('api/', get_schema_view(
        title= 'IKOKAZI Kenya',
        description = 'Api for ikokazi data',
        version = '1.0.0',))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
