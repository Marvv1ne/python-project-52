from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    USERNAME_FIELD = 'username'
