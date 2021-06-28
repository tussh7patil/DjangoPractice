from django.shortcuts import render

# Create your views here.
def showIndex(request):
    student_info = {"data":
                    [{"idno":101, "name":"Suresh", "marks":[50,46,74,65,55]},
                     {"idno":102, "name":"Rakesh", "marks":[55,78,64,69,45]},
                     {"idno":103, "name":"Mangesh", "marks":[59,86,79,66,74]},
                     {"idno":104, "name":"Vighnesh", "marks":[60,49,88,85,67]},
                     {"idno":105, "name":"Lokesh", "marks":[70,66,82,68,77]},
                     {"idno":106, "name":"Yadnesh", "marks":[80,77,74,99,66]},
                     {"idno":107, "name":"Yogesh", "marks":[90,46,74,65,55]},
                        ]
                    }
    return render(request,"index.html",student_info)
