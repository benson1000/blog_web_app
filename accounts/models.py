from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin,)

class CustomUserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """create and return a new super user"""
        user=self.create_user(email, password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    name = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD = 'email'

