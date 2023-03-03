from rest_framework import serializers
from .models import *
# Create your views here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'