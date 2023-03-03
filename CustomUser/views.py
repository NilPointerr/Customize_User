from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from django.contrib.auth import authenticate
from django.views.generic import CreateView,View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated 

class ModelViewSet_1(ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class Create_1(CreateView):

    template_name = 'auth.html'
    model = Student
    fields = '__all__'
    success_url = '/login'

class Login_1(CreateView):
    template_name = 'login.html'
    model  = Login
    fields = '__all__'
    success_url = '/create'
