# Generated by Django 4.2.1 on 2023-06-17 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_producer_alter_film_release_date_film_producers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.date(2023, 6, 17)),
        ),
    ]
