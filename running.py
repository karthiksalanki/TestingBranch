# myscript.py

# import os
# from django.conf import settings

# # Set your Django settings here
# settings.configure(
#     DEBUG=True,
#     INSTALLED_APPS=[
#         'userapp',
#     ],
#     # ... other settings ...
# )

# # Ensure the DJANGO_SETTINGS_MODULE environment variable is set
# os.environ['DJANGO_SETTINGS_MODULE'] = 'sellerprojecr.settings'

from datetime import  datetime
from userapp.models import Auction,Bidd
import pytz

utc=pytz.UTC

# Running file 
def main():
    currenttime = datetime.now().replace(tzinfo=utc)
    auctions = Auction.objects.filter(winner=None)
    for auction in auctions:
        if auction.end_time.replace(tzinfo=utc) < currenttime:
            bids=Bidd.objects.filter(auction=auction).order_by('-amount')[0]
            auction.winner = bids.user
            auction.final_amount = bids.amount
            auction.save()
        
if __name__ == '__main__':
    main()