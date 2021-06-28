from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request, "index.html")

def showWelcome(request):
    name = request.POST.get("t1")
    pwd = request.POST.get("t2")
    if name == "tushar" and pwd == "patil" :
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")