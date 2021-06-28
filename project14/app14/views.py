from django.shortcuts import render
from django.shortcuts import HttpResponse
from app14.models import Registration

def showIndex(request):
    return render(request,"index.html")

def showRegister(request):
    if request.method == "POST" :
        na=request.POST.get("name")
        con=request.POST.get("cno")
        loc = request.POST.get("location")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        # in models.py Registration table is created
        # To save the record in edusmart database
        Registration(name=na, contact=con, location=loc, email=email, password=pwd).save()
        return render(request, "registration.html",{"message":"Registration successful"})
    else:
     return render(request, "registration.html")             # method is GET type

def showLogin(request):
    return render(request, "login.html")