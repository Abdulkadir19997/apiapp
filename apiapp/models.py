from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError('User must have a valid email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, surname, password):
        user = self.create_profile(email, name, surname, password)
        user.is_superuser = True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255, unique=True)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'name'  #admine ozel
    REQUIRED_FIELDS = ['email','surname'] #profile olustururken fieldlerin sahip olacaklari bir ozelliktir

    def return_fullname(self):
        return self.name + ' ' + self.surname

    def return_shortname(self):
        return self.name

    def __str__(self):
        return self.name
