from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from MyProjectRegularExam.account.models import Profile


def validate_year(value):
    if not (1999 <= value <= 2030):
        raise ValidationError('Year must be between 1999 and 2030!')

# Create your models here.
class Car(models.Model):
    MAX_LENGTH_TYPE = 10
    MAX_LENGTH_MODEL = 15
    MIN_LENGTH_MODEL = 1
    MIN_PRICE = 1.0

    CAR_TYPES = {
        "_RALLY": "Rally",
        "OPEN_WHEEL": "Open-wheel",
        "KART": "Kart",
        "DRAG": "Drag",
        "OTHER": "Other"
    }

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        null=False,
        blank=False,
        choices=CAR_TYPES
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_MODEL,
        validators=[MinLengthValidator(MIN_LENGTH_MODEL)]
    )

    year = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[validate_year, MinValueValidator(1999), MaxValueValidator(2030)]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        default="https://...",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(MIN_PRICE)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False
    )