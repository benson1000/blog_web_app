from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .forms import SignUpForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    ordering=['id']
    list_display=['name', 'email', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    readonly_fields=['last_login']

admin.site.register(models.CustomUser, CustomUserAdmin)
