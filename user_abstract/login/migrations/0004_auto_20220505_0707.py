# Generated by Django 3.1 on 2022-05-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20220505_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='passwod',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]