from django.db import models
from django.contrib.auth.models import User,auth


# Create your models here.

# To create auction
class Auction(models.Model):
    item_name = models.CharField(max_length=150)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    bidd_count = models.PositiveIntegerField(default=0)
    winner = models.CharField(max_length=150,blank=True,null=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    
    class Meta:
        verbose_name = 'Auctions'
        verbose_name_plural = 'Auctions' 

    def __str__(self):
        return  self.item_name
    
    
# Bidds
class Bidd(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    applied_at = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Bidds'
        verbose_name_plural = 'Bidds' 

    def __str__(self):
        return  str(self.amount)
    
    