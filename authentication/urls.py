from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
path('', views.homepage, name="homepage"),
path('rest_prem',views.rest_prem,name="rest_prem"),
path('signup', views.signup, name="signup"),
path('signout', views.signout, name="signout"),
path('signin', views.signin, name="signin"),
path('homepage', views.homepage, name="homepage"),
path('team',views.rest_prem,name="team"),
path('my_team_stats',views.my_team_stats, name="my_team_stats"),
path('my_fixtures',views.my_fixtures, name="my_fixtures"),
path('my_minutes',views.my_minutes, name="my_minutes"),
path('my_shooting',views.my_shooting, name="my_shooting"),
path('fixtures',views.fixtures,name="fixtures"),
path('squad_stats',views.squad_stats,name="squad_stats"),
]