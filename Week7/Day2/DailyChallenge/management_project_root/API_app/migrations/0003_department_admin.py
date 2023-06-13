# Generated by Django 4.2.2 on 2023-06-13 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API_app', '0002_alter_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
