# Generated by Django 2.1.5 on 2020-07-05 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20200702_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 15, 28, 52, 619220), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 15, 28, 52, 620220), verbose_name='Tender Updated'),
        ),
    ]
