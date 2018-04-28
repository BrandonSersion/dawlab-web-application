"""DAWLAB_SITE URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

from content.views import home_page
from content import urls as content_urls
from authentication import urls as authentication_urls

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^content/', include(content_urls)),
    url(r'^authentication/', include(authentication_urls)),
    url(r'^admin/', admin.site.urls),
]
