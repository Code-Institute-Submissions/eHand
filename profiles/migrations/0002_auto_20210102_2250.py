# Generated by Django 3.1.4 on 2021-01-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='time_balance',
            field=models.DecimalField(choices=[('Not Specified', '0'), ('8 Hours', '8'), ('7 Hours', '7'), ('5 Hours', '5'), ('2 Hours', '2'), ('6 Hours', '6'), ('1 Hour', '1'), ('3 Hours', '3'), ('4 Hours', '4')], decimal_places=2, default='Not Specified', max_digits=4, max_length=40),
        ),
    ]
