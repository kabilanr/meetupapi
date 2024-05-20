from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def index(request):
    if request.method=="POST":
        jsondata=JSONParser().parse(request)
        print(jsondata)
        username = jsondata.get('username')
        password = jsondata.get('password')
        print(f"user name:{username}")
        print(f"password:{password}")
        return HttpResponse("data posted")


    return HttpResponse("hello there")
