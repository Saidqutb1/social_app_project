from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUSer(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, default='default_images/user_image.png')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


