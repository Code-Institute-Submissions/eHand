# Generated by Django 3.1.4 on 2021-02-11 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0008_auto_20210211_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='event_date',
        ),
        migrations.AddField(
            model_name='notice',
            name='event_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Event Date'),
        ),
    ]