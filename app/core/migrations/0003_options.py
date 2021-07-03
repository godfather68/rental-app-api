# Generated by Django 3.2 on 2021-07-03 09:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_rooms', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
                ('furnished', models.BooleanField(default=False)),
            ],
        ),
    ]
