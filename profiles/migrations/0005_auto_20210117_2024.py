# Generated by Django 3.1.4 on 2021-01-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210114_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='time_balance',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]
