from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.team_page, name='team'),
    url(r'^(?P<pk>\d+)/$', views.team_profile_pages, name='team_profiles'),
]