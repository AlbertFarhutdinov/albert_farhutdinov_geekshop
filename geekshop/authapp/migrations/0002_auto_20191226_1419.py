# Generated by Django 2.2.5 on 2019-12-26 11:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 28, 11, 19, 20, 706604, tzinfo=utc)),
        ),
    ]
