# Generated by Django 2.1.5 on 2020-07-01 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200701_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 26, 8, 832042), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 26, 8, 833045), verbose_name='Tender Updated'),
        ),
    ]