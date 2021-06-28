from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":             # for submit button method is post
        name = request.POST.get("t1")
        pwd = request.POST.get("t2")
        if name == "tushar" and pwd == "patil":
            return render(request,"index.html",{"message":"valid"})
        else:
            return render(request,"index.html",{"message":"invalid"})
    if request.method == "GET":             # for url method is get
        return render(request, "index.html")