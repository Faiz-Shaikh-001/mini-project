from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, SignupForm
from .models import CustomUser


def home(request):
    login_form = LoginForm()
    signup_form = SignupForm()
    return render(request, 'signup/index.html', {'form': login_form, 'form': signup_form})



def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            existing_user = CustomUser.objects.filter(email=email).first()
            
            if existing_user is not None:
                if existing_user.username == username:
                    messages.info(request, 'Username already exists')
                elif existing_user.role == role:
                    messages.error(request, 'User with the same email and role already exists')
                else:
                    myuser = CustomUser.objects.create_user(username, email, password)
                    myuser.role = role
                    myuser.save()
                    messages.success(request, 'Your account has been successfully created.')
            else:
                myuser = CustomUser.objects.create_user(username, email, password)
                myuser.role = role
                myuser.save()
                messages.success(request, 'Your account has been successfully created.')
        else:   
            return HttpResponse('error occured')
    else:
        form = SignupForm()
    
    return render(request, 'signup/index.html', {'form': form, 'messages': messages.get_messages(request)})







def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            print(role)

            if role == 'admin':
                return redirect('admin-page')
            elif role == 'user':
                return redirect('user-page')
            else:
                return HttpResponse('Incorrect Role')
        else:
            print(form.errors)
    else:
        return redirect('home')



def logout(request):
    pass