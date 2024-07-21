from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()


# def receipe(request):
#     return render(request,"receipe.html")
    # return HttpResponse("<h1>successfully receipe </h1>")


# @login_required()
def receipes(request):
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        name=data.get("name")
        description=data.get("description")
        print(name)
        print(description)
        print(image)
        
        Receipe.objects.create(
            name=name ,
            image=image ,
            description=description ,
            )
        return redirect('/receipes')
    query_set= Receipe.objects.all()  
    if request.GET.get("search"):
        query_set=query_set.filter(name__icontains= request.GET.get("search"))
   

    context={"receipe":query_set}      
    return render(request,"receipes.html",context)


# def receipe_delete(request,id):
#     print(id)
#     return HttpResponse("a")

# @login_required
def success_page(request):
    return HttpResponse("<h1> you come here successfully welcome i am varun gupta </h1> ")

def receipe_update(request,id):
    query_set=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        name=data.get("name")
        description=data.get("description")
        query_set.name=name
        query_set.description =description
        if image:
            query_set.image=image
        query_set.save()
        return redirect("/receipes")

        
        
    context={"receipe":query_set}      
    return render(request,"update-receipe.html",context)
    


def receipe_delete(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes")

def login_page(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"username does not existes")
            return redirect("/login/")
        
        user= authenticate(username=username,password=password)
    
        if user is None:
            messages.error(request,"invalid passward")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect("receipes/")
    return render(request , "login.html")



def regester_page(request):
    
    if request.method=="POST":
        first_name  = request.POST.get("first_name")
        last_name   = request.POST.get("last_name")
        password    = request.POST.get("password")
        username    = request.POST.get("username")
        
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request,"username already exist")
            return redirect("/regester/")
        
        user= User.objects.create(
            first_name  =first_name  , 
            last_name   =last_name   , 
            username    =username    
        )
        
        
        user.set_password(password)
        user.save()
        messages.info(request,"account created succesfully ")

        return redirect("/regester/")




    return render(request,"regester.html")


def logout_page(request):
    logout(request)
    return redirect("/login")