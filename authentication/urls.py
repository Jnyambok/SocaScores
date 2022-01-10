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
path('fixtures',views.fixtures,name="fixtures"),
path('squad_stats',views.squad_stats,name="squad_stats"),
]