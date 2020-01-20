from django.shortcuts import render
from .models import destination

# Create your views here.
from django.http import HttpResponse


def index(request):
    dests= destination.objects.all()

    return render(request,"index.html",{"dests": dests})



