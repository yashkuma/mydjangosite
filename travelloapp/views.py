from django.shortcuts import render
from .models import destination

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. Welcome to your first test App Yash! You're at the polls index.")
    #dest = ['Shimla','Pune','Banguluru']
    dest1 = destination()
    dest1.name='Shimla'
    dest1.desc='Nature is here'
    dest1.img='destination_1.jpg'
    dest1.price='400'
    dest1.offer= False

    dest2 = destination()
    dest2.name='Hydrabad'
    dest2.desc='Biryani is here'
    dest2.img='destination_4.jpg'   
    dest2.price='500'
    dest2.offer= False

    dest3 = destination()
    dest3.name='Haridwar'
    dest3.desc='God is here'
    dest3.img='destination_6.jpg'
    dest3.price='200'
    dest3.offer= True

    dests= [dest1, dest2, dest3]

    return render(request,"index.html",{"dests": dests})

