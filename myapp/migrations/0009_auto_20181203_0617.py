# Generated by Django 2.1.3 on 2018-12-03 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20181112_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 3, 6, 17, 31, 107125, tzinfo=utc)),
        ),
    ]