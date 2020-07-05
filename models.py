from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Item(models.Model):
    item_no = models.CharField(max_length=200, primary_key = True )
    item_name = models.CharField(max_length = 200)
    item_quantity = models.CharField(max_length = 200, default = 0)
    item_description = models.TextField(blank = True)
    item_updated = models.DateTimeField("Item updated", default=datetime.now())
    item_price = models.CharField(max_length = 100, default = 0)

    def __str__(self):
        return self.item_name

class TenderEstimate(models.Model):
    est_no = models.CharField(max_length = 100, verbose_name = 'Estimate Number')
    est_desc = models.TextField(blank = True)
    tender_no = models.ForeignKey('Tender', on_delete = models.CASCADE)
    def __str__(self):
        return self.est_no

class Tender(models.Model):
    tender_no = models.CharField(max_length = 100)
    tender_order = models.CharField(max_length =200)
    tender_updated = models.DateTimeField("Tender Updated", default=datetime.now())
    tender_start_date = models.DateTimeField()

    On_Going = 'OG'
    Completed = 'CM'
    tender_status_CHOICES = [
        (On_Going, 'On going'),
        (Completed, 'Completed')
    ]
    tender_status = models.CharField(
        max_length = 2,
        choices = tender_status_CHOICES,
        default = On_Going,
    )

    def __str__(self):
        return self.tender_no

class EstimateItem(models.Model):
    item_name = models.ForeignKey('Item', on_delete = models.CASCADE)
    item_qty = models.CharField(max_length = 20, verbose_name = "Item Quantity Needed")
    qty_cus = models.CharField(max_length = 20, verbose_name = "Quantity provided by customer")
    qty_con = models.CharField(max_length = 20, verbose_name = "Quantity provided by contractor")
    est_no = models.ForeignKey('Estimate', on_delete=models.CASCADE)

class Estimate(models.Model):
    est_no = models.ForeignKey('TenderEstimate', on_delete = models.CASCADE, verbose_name = 'Estimate Number')

    def __str__(self):
        return str(self.est_no)


