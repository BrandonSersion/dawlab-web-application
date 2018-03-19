from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^team/$', views.team_page, name='team'),
    url(r'^team/(?P<pk>\d+)/$', views.team_profile_pages, name='team_profiles'),
    url(r'^login/$', views.employee_login_page, name='login'),
]