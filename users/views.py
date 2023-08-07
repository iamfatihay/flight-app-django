from django.shortcuts import render
# Create your views here.
from rest_framework.generics import (CreateAPIView)
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view
class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer