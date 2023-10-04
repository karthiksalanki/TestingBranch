from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class AuctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'
        
class BiddSerializers(serializers.ModelSerializer):
    auction = AuctionSerializers
    class Meta:
        model = Bidd
        fields = '__all__'
        
class AuctionlistSerializers(serializers.ModelSerializer):
    bid = BiddSerializers()
    class Meta:
        model = Auction
        fields = ['item_name','start_price','start_time','end_time','bidd_count','winner','final_amount','bid']