from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.
#from django.http import HttpResponse

#simple registration page 
def register(request):

    if request.method== 'POST':
        fname= request.POST['first_name']
        lname= request.POST['last_name']
        uname= request.POST['username']
        email= request.POST['email']
        passwd= request.POST['passwd']
        c_passwd= request.POST['c_passwd']
        
        if passwd == c_passwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exists')
                return redirect('register')
                
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
                
            else:
                user= User.objects.create_user(username=uname, email=email,first_name=fname,last_name=lname,password=passwd)
                user.save()
                messages.info(request,'Congratutions !! User is Registered successfully')
                return redirect('/')


        else:
            messages.info(request,'Error ! Password does not match')
            return redirect('register')


        #return redirect ('/')

    else:
        return render(request,"register.html")



