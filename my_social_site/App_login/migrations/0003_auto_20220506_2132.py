# Generated by Django 3.1.11 on 2022-05-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]