from rest_framework import serializers
from profile_site.models import ProfileUser


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'email', 'phone_number', 'address', 'inn')
