# Generated by Django 3.2.9 on 2021-12-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mift', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('Fund', 'Fund'), ('Volunteering', 'Volunteering')], max_length=20),
        ),
    ]
