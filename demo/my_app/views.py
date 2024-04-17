from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'prathi'})

def add(request):
    first_value=int(request.POST['number1'])
    second_value=int(request.POST['number2'])
    final_result = first_value+second_value

    return render(request,"result.html",{'result':final_result})

def index(request):
   print(request.headers)

@login_required
def template(request):
    new_list=["apple","mango","grapes"]
    new_dict={
        "name":"prathi",
        "age":22
    }
    items=["grapes","orange","guava"]
    username = request.user.username
    return render(request,'index.html',{'username':username,'new_list':new_list, 'new_dict':new_dict,'items':items})


