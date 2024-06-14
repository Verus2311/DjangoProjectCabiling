from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.helloWorld, name = "helloWorld"),
     path("testpath/",views.testpath, name = "testPath")

]
   
