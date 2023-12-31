from django.urls import path
from .views import *


urlpatterns = [
    #user management
    path('user/',createuser,name='login'),
    path('login/',login,name='login'),
    path('update/<int:id>',updateuser,name='updateuser'),
    path('logout/',logout_view,name='logout'),
    #auction
    path('auctions/',auctionlist,name='auctionlist'),
    path('auctions/complete/',updateauction,name='auctionlist'),
    #bids
    path('bids/',createbid,name='createbid'),
    
]