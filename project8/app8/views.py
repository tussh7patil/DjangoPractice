from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showIndex(request):
    return render(request, "index.html")

def showData(request):
    na = request.POST.get("t1")
    snm = request.POST.get("t2")
    message = "welcome "+na+" "+snm
    return HttpResponse(message)