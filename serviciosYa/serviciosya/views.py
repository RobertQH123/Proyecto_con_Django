from django.shortcuts import render

def myHome(request , *args, **kwargs):
    return render(request,"inicio.html",{})