from django.shortcuts import render
from django.http import HttpResponse


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
 