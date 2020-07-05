from django.contrib import admin
from .models import Item, Tender, TenderEstimate, Estimate, EstimateItem
from django.db import models


# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title/date', {
            'fields': (('item_no', 'item_name', 'item_quantity'), 'item_updated')
        }),
        ('Content', {
            'fields': ('item_description',)
        })
)
    list_display = ('item_name', 'item_no', 'item_quantity')
    ordering = ("item_name",)

class TenderEstimateInline(admin.StackedInline):
    model = TenderEstimate
    extra = 1

class TenderAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Title", {
            "fields": (("tender_no", "tender_order"),"tender_status", "tender_updated" )
        }),
        ("Dates", {
            "fields": ("tender_start_date",)
        }),
    )
    inlines = [TenderEstimateInline]

    list_display = ('tender_order', 'tender_no',)
    ordering = ("-tender_no",)
    search_fields = ('tender_no', 'tender_order')

class EstimateItemInline(admin.TabularInline):
    model = EstimateItem
    extra = 1

class EstimateAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Title", {
            "fields": ('est_no',)
        }),
    )
    inlines = [EstimateItemInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Tender, TenderAdmin)
admin.site.register(Estimate, EstimateAdmin)