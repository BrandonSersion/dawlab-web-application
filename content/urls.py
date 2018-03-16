from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^our_team/', views.our_team_page, name='our_team'),
]