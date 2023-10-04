from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db.models import Max
from userapp.serializers import *
from datetime import datetime
import json
import pytz

utc=pytz.UTC
# Create your views here.



#Read and Create user
@api_view(['POST','GET'])
@csrf_exempt
def createuser(request):
    try:
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializers(users, many=True)
            return Response({"status":200,"data":serializer.data})
        else:
            requestdata = json.loads(request.body)
            data={
            "username" : requestdata['username'],
            "first_name" : requestdata['firstname'],
            "last_name" : requestdata['lastname'],
            "email" : requestdata['email'],
            "password": requestdata['password']}
            print(data)
            user = User.objects.create_user(**data)
            return Response({"status":201,"username":user.username,"password":user.password})
    except Exception as e:
        return Response(str(e))

#Update and Delete user
@api_view(['PUT','DELETE'])
@csrf_exempt
def updateuser(request,id):
    if request.method == 'PUT':
        requestdata = json.loads(request.body)
        data={
            "username" : requestdata['username'],
            "first_name" : requestdata['firstname'],
            "last_name" : requestdata['lastname'],
            "email" : requestdata['email'],
            "password": requestdata['password']}
        print(data)
        user=User.objects.filter(id=id).update(**data)
        serialize = UserSerializers(user)
        if serialize.is_valid():
            return Response({'data':serialize.data})
        else:
            return Response({'data':serialize.error_messages})
    else:
        user=User.objects.get(id=id)
        user.delete()
        return Response({'status':200})
            
        
        
    
    
#token authentication
@api_view(['POST'])
@csrf_exempt
def login(request):
    #try:
    requestdata = json.loads(request.body)
    username = requestdata['username']
    #email = requestdata.get('email')
    password = requestdata['password']
    user = authenticate(request,username=username, password = password)     #User.objects.get(username=username,password=password) 
    print(user,username,password)
    if user is not None:
        print("login")
        auth.login(request,user)
        print('login sucssfully')
        print(user,username,password)
        token,created=Token.objects.get_or_create(user=user)
        # token = Token.objects.filter(user_id=request.user)          #get_or_create(user = user)
        # if token is None:
        #     token=Token.objects.create(user=user)
        print(username,password,token.key)
        return Response({"status":200,"token":token.key, "username":username, "password":password})
    else:
        return Response({"status":400,"data":"invalid user"})
    # except Exception as e:
    #     return Response(str(e))

#logout
@api_view(['GET'])
def logout_view(request):
    try:
        auth.logout(request)
        return Response({'status':200, 'data':'logout successfully'})
    except Exception as e:
        return Response({'status':500, 'data':str(e)})
    
# Auction List
@api_view(['GET'])
@csrf_exempt
def auctionlist(request):
    try:
        auctiondata = Auction.objects.all().order_by('-id')
        serializer = AuctionSerializers(auctiondata, many=True)
        return Response({'status':200,'data':serializer.data})
    except Exception as e:
        return Response(str(e))

# Create Bid
@api_view(['POST'])
@csrf_exempt
def createbid(request):
    #try:
    if request.method == 'POST':
        requestdata = json.loads(request.body)
        currenttime = datetime.now().replace(tzinfo=utc)
        auction=requestdata['auction']
        auctionobj=Auction.objects.get(item_name=auction)
        user=User.objects.get(username=request.user)            #basic auth
        endtime = auctionobj.end_time.replace(tzinfo=utc)
        print(auctionobj,user,auctionobj.end_time,endtime,currenttime)
        if endtime > currenttime:
            biddata = Bidd.objects.create(user=user,auction=auctionobj,amount=requestdata['amount'])
            auctionobj.bidd_count=auctionobj.bidd_count+1
            auctionobj.save()
            return Response({'status':201,'data':"bid created successfully"})
        else:
            return Response({'data':"Auction is closed"})
    # except Exception as e:
    #     return Response(str(e))
            
    
@api_view(['GET'])
@csrf_exempt
def updateauction(request):
    currenttime = datetime.now().replace(tzinfo=utc)
    auctions = Auction.objects.filter(winner=None)
    print(auctions)
    for auction in auctions:
        print(currenttime,auction.end_time)
        if auction.end_time.replace(tzinfo=utc) < currenttime:
            bids=Bidd.objects.filter(auction=auction).order_by('-amount')[0]   
            if bids is not None:
                auction.winner = bids.user.username
                auction.final_amount = bids.amount
                auction.save()
                print('updated',bids)
            else:
                print('not updated')
    return Response({'status':200})
            
        
