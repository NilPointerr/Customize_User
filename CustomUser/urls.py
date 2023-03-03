from django.contrib import admin
from django.urls import path
from .views import Create_1,Login_1
from CustomUser.auth import CustomAuthToken
urlpatterns = [
   path('create',Create_1.as_view(),name='create'),
   path('login',Login_1.as_view(),name='login'),
   path('gettoken',CustomAuthToken.as_view(),name='gettoken')
]
