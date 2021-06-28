from django.shortcuts import render

def showIndex(request):
    emp_detail={"id":101,"name":"Ravi","salary":185000.00,
                "designation":"Manager","componey":"IBM",}
    return render(request,"main.html",emp_detail)
