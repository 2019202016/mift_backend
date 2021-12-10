# Generated by Django 3.2.9 on 2021-12-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('NGO', 'ngo'), ('Volunteer', 'volunteer')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
