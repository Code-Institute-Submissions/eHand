# Generated by Django 3.1.4 on 2021-02-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0009_auto_20210203_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_type',
            field=models.CharField(choices=[('Free', 'free'), ('Premium', 'prem')], default='Free', max_length=40),
        ),
    ]