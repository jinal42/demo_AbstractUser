    # Generated by Django 3.1 on 2022-05-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20220505_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='passwod',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
