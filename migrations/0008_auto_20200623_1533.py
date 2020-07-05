# Generated by Django 2.1.5 on 2020-06-23 10:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200623_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='tender_materials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 15, 33, 0, 910519), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 15, 33, 0, 911520), verbose_name='Tender Updated'),
        ),
    ]