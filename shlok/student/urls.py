from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path("save/<int:id>/<str:name>/<int:age>/<int:T_mark>", views.save ,name='saveStudent'),
    path("getallstudent", views.get_allStudent ,name='getallStudent'),
    path("getstudent/<str:name>", views.getStudent ,name='getStudent'),

    path("deletestudent/<str:name>", views.deleteStudent, name='deleteStudent'),

    path("perstudent", views.percentage, name='Studentper'),
    path("Addaddress/<int:id>/<str:address>", views.saveAddress ,name='address')

]
