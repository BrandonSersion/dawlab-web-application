from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.authentication_page, name='authentication'),
    url(r'^employee_zone/', views.employee_zone_page, name='employee_zone'),
]