from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homepage(request):
    #return HttpResponse("Hello, world. Welcome to your first test App Yash! You're at the polls index.")
    return render(request,"app.html")

def add(request):
    #var1=request.GET["FirstName"]
    #var2=request.GET["LastName"]
    var1=request.POST["FirstName"]
    var2=request.POST["LastName"]

    res= var1+" "+ var2
    return render(request,"result.html", {"result": res} )

