# Generated by Django 2.1.7 on 2019-04-09 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jit', '0006_auto_20190406_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 17, 24, 48, 23332, tzinfo=utc)),
        ),
    ]
