# Generated by Django 4.2.2 on 2023-06-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='vacancy',
            field=models.BooleanField(default=False),
        ),
    ]
