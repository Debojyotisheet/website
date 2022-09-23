from django.shortcuts import render,HttpResponse
from home.models import Contact
def page(request):
    context={'name':'Debojyoti','Subject':'MCA'}
    return render(request,'home.html',context)
    #return HttpResponse("This si a page inside the website")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about me")
def contact(request):
    #contact={'contact':7362956048,'city':'Contai','pin':721433,'road':'Majna road'}
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["number"]
        email=request.POST["email"]
        details=request.POST["details"]
        ins=Contact(name=name,phone=phone,email=email,details=details)
        ins.save()
        print("The data has been Written in the DataBase")
    return render(request,'contact.html')
    #return HttpResponse("This is my contact")
def projects(request):
    return render(request,'projects.html')
    #return HttpResponse("This is all the projects that i have made")