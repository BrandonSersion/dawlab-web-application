from django.conf.urls import url, include
from content import views
from authentication import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.authentication_page, name='authentication'),
]