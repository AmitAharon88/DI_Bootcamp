# Generated by Django 4.2.1 on 2023-06-01 16:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_person_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
