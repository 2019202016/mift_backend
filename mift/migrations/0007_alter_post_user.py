# Generated by Django 3.2.9 on 2021-12-08 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mift', '0006_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
