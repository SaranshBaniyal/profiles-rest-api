from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        #is_superuser is present in the PermissionMixin class, which is inherited
        user.is_superuser = True
        #is_staff is present in the UserProfile class that we created
        user.is_staff = True
        user.save(using=self._db)
        
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #triple quotes are used here like anotations for improved readability
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #overriding the USERNAME_FIELD of AbstractBaseUser with email
    USERNAME_FIELD = 'email'
    #email is now already required due to above line
    REQUIRED_FIELDS = ['name']

#self is the first argument for all the functions inside a class
    def get_full_name(self):
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
        #since we dont have any shorter name available at hand

#This function tells what to return whenever we convert UserProfile class's object to a string
#in this case it will return email
#this function is recommended to add so that whenever we convert this object to string, it returns something meaningful
    def __str__(self):
        """Return string representation of the user"""
        return self.email