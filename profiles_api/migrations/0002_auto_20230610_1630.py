# Generated by Django 2.2 on 2023-06-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]