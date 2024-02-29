from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django import forms

# Create your models here.

MIN_LENGTH_USERNAME = 3
MAX_LENGTH_USERNAME = 15
def validate_username(username):
    is_valid = all(ch.isalnum() or ch== '_' for ch in username)
    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")

def validate_username_length(username):
    if len(username) < MIN_LENGTH_USERNAME:
        raise ValidationError("Username must be at least 3 chars long!")

class Profile(models.Model):
    MIN_AGE_PROFILE = 21
    MAX_PASSWORD_LENGTH = 20
    MAX_LENGTH_FIRST_NAME = 25
    MAX_LENGTH_LAST_NAME = 25

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_USERNAME,
        validators=[validate_username,MinLengthValidator(MIN_LENGTH_USERNAME)],
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(MIN_AGE_PROFILE)],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        #widget=forms.PasswordInput,
        max_length=MAX_PASSWORD_LENGTH
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGTH_FIRST_NAME,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGTH_LAST_NAME,
    )

    profile_image = models.ImageField(
        blank=True,
        null=True,
    )



