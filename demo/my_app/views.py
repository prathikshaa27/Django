from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


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

def new_view(request):
    response = HttpResponse("Prathi", content_type='text/plain',status=200)
    response['X-My-header']='New value'
    content_type=response['Content-Type']

    contains_content_type=response.has_header('Content-Type')
    headers =response.items()
    response.setdefault('Content-Type', 'text/html')
    response.set_cookie('user-id','123',max_age=85)
    #return response

data = {
    "Name":"Prathi",
    'status':"success"
}
response = JsonResponse(data)

