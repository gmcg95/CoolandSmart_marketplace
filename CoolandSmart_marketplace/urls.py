"""
URL configuration for CoolandSmart_marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')).
"""
from django.contrib import admin
from django.urls import path, include
from CoolandSmart_marketplace import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),                  # admin
    path('', include('CSapp.urls')),                  # CSapp URLs
    path('', include('accounts_app.urls')),           # accounts_app URLs 
    path('', include('products_app.urls')),           # products_app URLs
    path('', include('django.contrib.auth.urls')),    # Django authentication URLs
]
if settings.DEBUG:  # verify if the project run in debug mode; helps with the errors management
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # includes the urls for media files
