from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import ExampleForm

# Create your views here.
def register(request):
  if request.method == "POST":
    username = request.POST['username'].lower()
    email = request.POST['email']
    password1 = request.POST['password']
    password2 = request.POST['re_password']
    
    if password1 == password2:
      if User.objects.filter(email=email).exists():
        print("email taken")
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        print("usrrname taken")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        return redirect('login')
    
  else:
    return render(request, 'register.html')
  
  
def login(request):
  if request.method == "POST":
    username = request.POST['your_name'].lower()
    password = request.POST['password']
    
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      print("invalid credentials")
      return redirect('login')
    
    
  else:
    return render(request,'login.html')
    
def logout(request):
  auth.logout(request)
  return redirect('/')
  

 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
  
  
