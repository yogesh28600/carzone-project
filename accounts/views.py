from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from inquiry.models import Inquiry
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request): 
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'accounts/login.html')
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request,'accounts/logout.html')
def register_user(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
                return redirect('register')
            else:
                User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                messages.success(request,'Registerd successfully')
                return redirect('login')
        else:
            messages.error(request,'Password didnot match')
            return redirect('register')
    return render(request,'accounts/register.html')
@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        inquiries = Inquiry.objects.order_by('-created_date').filter(user_id = request.user.id)
        print(inquiries)
        data = {
            'inquiries':inquiries,
        }
    return render(request,'accounts/dashboard.html',data)