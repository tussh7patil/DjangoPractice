from django.http import HttpResponse
def showIndex(request):
    message=" hello world"
    return HttpResponse(message)
