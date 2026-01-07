from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serial=studSerial(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getstid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    serial=studSerial(stid)
    return Response(data=serial.data)
 
@api_view(['DELETE','GET'])
def deletestid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studSerial(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)  

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=studSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_BAD_REQUEST)

@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method=='GET':
        serial=studSerial(stid)
        return Response(data=serial.data)
    
    if request.method=='PUT':
        serial=studSerial(data=request.data,instance=stid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

      

