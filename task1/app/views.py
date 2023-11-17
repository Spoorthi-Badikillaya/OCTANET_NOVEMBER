from django.shortcuts import render
def home(request):
    return render(request,'app/home.html')
def aboutus(request):
    return render(request,"app/aboutus.html")
def register(request):
    return render(request,"app/auth/register.html")
def loginpage(request):
    return render(request, "app/auth/login.html")






# Create your views here.
