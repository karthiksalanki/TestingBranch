from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display =  ['__all__']
    search_fields = ['item_name']
    
    
admin.site.register(Bidd)
class BiddAdmin(admin.ModelAdmin):
    list_display =  ['__all__']
    search_fields = ['amount']