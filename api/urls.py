from django.urls import path
from .views import *

app_name = 'api'


urlpatterns = [
    path('profile/create/', NewUserProfileApi.as_view(), name='create_profile')
]
