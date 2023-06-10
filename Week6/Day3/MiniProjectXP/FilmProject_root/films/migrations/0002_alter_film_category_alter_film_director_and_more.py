# Generated by Django 4.2.1 on 2023-06-08 09:23

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(related_name='films', to='films.category'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(related_name='films', to='films.director'),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.date(2023, 6, 8)),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
        ),
    ]
