# Generated by Django 3.1.4 on 2021-02-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_commitments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='event_date_time',
            field=models.DateTimeField(verbose_name='Event Date'),
        ),
    ]
