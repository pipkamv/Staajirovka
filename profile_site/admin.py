from django.contrib import admin
from .models import ProfileUser


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'phone_number']


admin.site.register(ProfileUser, ProfileUserAdmin)
