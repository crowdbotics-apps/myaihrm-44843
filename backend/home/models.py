from django.conf import settings
from django.db import models


class User(models.Model):
    "Generated Model"
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    is_active = models.BooleanField(
        default="True",
    )
    is_staff = models.BooleanField(
        default="False",
    )
    is_superuser = models.BooleanField(
        default="False",
    )
