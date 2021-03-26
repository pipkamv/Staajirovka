from django.shortcuts import render
from rest_framework import generics
from api.serializers import ProfileCreateSerializer


class NewUserProfileApi(generics.CreateAPIView):
    serializer_class = ProfileCreateSerializer


