# Generated by Django 4.2.1 on 2023-06-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_alter_address_address_alter_address_address2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]