# Generated by Django 2.1.5 on 2020-07-01 16:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200630_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_no', models.CharField(max_length=100, verbose_name='Estimate No.')),
                ('est_desc', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 21, 32, 25, 991003), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 21, 32, 25, 992002), verbose_name='Tender Updated'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='tender_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tender'),
        ),
    ]