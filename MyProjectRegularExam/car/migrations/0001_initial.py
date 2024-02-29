# Generated by Django 5.0.2 on 2024-02-24 09:23

import MyProjectRegularExam.car.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('_RALLY', 'Rally'), ('OPEN_WHEEL', 'Open-wheel'), ('KART', 'Kart'), ('DRAG', 'Drag'), ('OTHER', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.PositiveIntegerField(validators=[MyProjectRegularExam.car.models.validate_year, django.core.validators.MinValueValidator(1999), django.core.validators.MaxValueValidator(2030)])),
                ('image_url', models.URLField(default='https://...', error_messages={'unique': 'This image URL is already in use! Provide a new one.'})),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
