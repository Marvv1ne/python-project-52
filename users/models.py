from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['username']
