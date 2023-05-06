from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *



urlpatterns = [
    path('',Home.as_view(),name='home' ),
    path('profile/',ProfileViews.as_view(),name='profile' ),
    path('login/',Login.as_view(),name='login' ),
    path('logout/',LogoutView.as_view(next_page='login' ),name='logout'),
    path('register/',Register.as_view(),name='register'),

]
