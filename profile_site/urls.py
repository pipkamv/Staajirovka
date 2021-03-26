from django.urls import path
from .views import profile, edit, register_user, index


app_name = 'profile'


urlpatterns = [
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit, name='edit'),
    path('', index, name='index'),
]
