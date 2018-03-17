from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^our_team/', views.our_team_page, name='our_team'),
    url(r'^employee_zone/', views.employee_zone_page, name='employee_zone'),
]