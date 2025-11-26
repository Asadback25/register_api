from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

ROLL_CHOICES = (
     ('admin', 'Admin'),
     ('user', 'Oddiy User'),
)

user_name_regex = RegexValidator(regex=r'^[A-Z]{3}[0-9]{2}[A-Z]{3}[0-9]{3}$',)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=11, unique=True, validators=[user_name_regex])
    email = models.EmailField(max_length=255, unique=True)
    role =models.CharField(choices=ROLL_CHOICES, default='user', max_length=10)
    def __str__(self):
        return self.username