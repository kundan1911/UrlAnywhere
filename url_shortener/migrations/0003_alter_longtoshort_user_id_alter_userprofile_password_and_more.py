# Generated by Django 4.1.3 on 2023-06-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_userprofile_longtoshort_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longtoshort',
            name='user_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]