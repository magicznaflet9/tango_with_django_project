from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {"boldmessage": "Creamy cupcake!"}
    return render(request,"rango/index.html",context=context_dict)

def about(request):
    context_dict = {"boldmessage": "This tutorial has been put together by Zofia"}
    return render(request,"rango/about.html",context=context_dict)

