from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth.models import User, auth
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def registration(request):
    if request.method=='POST':
        first_name=request.POST.get['first_name']
        last_name = request.POST.get['last_name']
        email = request.POST.get['email']
        username = request.POST.get['username']
        password = request.POST.get['password']
        password_confirm = request.POST.get['password_confirm']
        if password==password_confirm:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('registration')
            else:

                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password_confirm)

                user.save();
                print("user created")
                return redirect('registration')
        else:
            # messages.info(request,"password not match!please renter")
            print("Password not matched")
            return redirect("registration")


    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Details')
            return redirect('login')
    else:
        return render(request,"logincart.html")
