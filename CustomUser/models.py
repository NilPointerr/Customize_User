from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager 
# Create your models here.
# import these for token generation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    username = None
    mobile = models.CharField (max_length=14)
    email = models.EmailField(unique=True)
    is_verified = models . BooleanField (default=False)
    email_oken = models.CharField (max_length=100, null=True, blank=True)
    forget_password = models.CharField (max_length=100, null=True , blank=True)
    last_login_time = models . DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField (null=True, blank=True)
    address = models.TextField(max_length=1000,default='')
     
    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=200)
    roll_no = models.CharField(max_length=3)
    mobile_no = models.CharField(max_length=10)

    

    def __str__(self):
        return self.name 

class Login(models.Model):

    name = models.CharField( max_length=50)
    password = models.CharField(max_length=4)

    def __str__(self):
        return self.name
    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created=False,*args, **kwargs):
    if created:
        Token.objects.create(user = instance)
        print(Token.objects.create(user = instance))

