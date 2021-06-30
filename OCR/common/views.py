from django.shortcuts import render
from student.models import RegistrationModel

# Create your views here.
def showIndex(request):
    return render(request, "common/index.html")

def studentPage(request):
    return render(request, "common/student.html")


def studenRegistration(request):
    if request.method == "POST":
        name_var = request.POST.get("student_name")
        contact_var = request.POST.get("student_contact")
        email_var = request.POST.get("student_email")
        pwd_var = request.POST.get("student_password")
        RegistrationModel(name=name_var,contact=contact_var,email=email_var,password=pwd_var).save()
        return render(request, "common/student.html", {"message": "Registration successful"})
    else:
        studentPage(request)