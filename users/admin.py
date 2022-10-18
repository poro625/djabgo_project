from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin) #유저의 경우에만 UserAdmin이 필요하다