# Generated by Django 3.1.4 on 2021-02-11 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0014_remove_notice_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='pref_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Preferred Date'),
        ),
    ]
