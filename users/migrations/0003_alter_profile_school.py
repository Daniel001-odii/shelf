# Generated by Django 4.0.3 on 2022-04-15 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_firstname_profile_lastname_profile_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.TextField(default=''),
        ),
    ]