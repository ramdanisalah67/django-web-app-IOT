from django.http import  HttpResponse

def index(request):
    return HttpResponse("hello,this is page index")

def sumCalc(request):
    return HttpResponse("sum is 10")
