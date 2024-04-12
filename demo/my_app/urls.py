from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add,name="add"),
    path('new_view/',views.new_view,name='new view')
   
]