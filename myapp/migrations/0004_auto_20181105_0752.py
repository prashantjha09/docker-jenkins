# Generated by Django 2.1.3 on 2018-11-05 07:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181105_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 5, 7, 52, 52, 297699, tzinfo=utc)),
        ),
    ]