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

    MIN_YEAR = 1999
    MAX_YEAR = 2030

    ERROR_MESSAGE_YEAR = f"Year must be between {MIN_YEAR} and {MAX_YEAR}!"

    CAR_TYPES = {
        "Rally": "Rally",
        "Open Wheel": "Open-wheel",
        "Kart": "Kart",
        "Drag": "Drag",
        "Other": "Other"
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

    year = models.IntegerField(
        validators=(MaxValueValidator(MAX_YEAR, message=ERROR_MESSAGE_YEAR),
                    MinValueValidator(MIN_YEAR, message=ERROR_MESSAGE_YEAR),),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,

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