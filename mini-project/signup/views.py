from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LoginForm, SignupForm

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Here, you can perform authentication and redirection logic based on the 'role'
            if role == 'admin':
                # Redirect to the admin page
                return render(request, 'adminpanel/dashboard.html')
            elif role == 'user':
                # Redirect to the user page
                return render(request, 'userpage/user-page.html')
        else:
            # Form validation errors occurred, handle them or return an error response
            return HttpResponse('error occured')
    else:
        form = LoginForm()
    
    return render(request, 'signup/signup.html', {'form': form})
    

def signup(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Here, you can perform authentication and redirection logic based on the 'role'
            if role == 'admin':
                # Redirect to the admin page
                return redirect('admin-page')
            elif role == 'user':
                # Redirect to the user page
                return redirect('user-page')
        else:
            # Form validation errors occurred, handle them or return an error response
            return HttpResponse('error occured')
    else:
        form = SignupForm()
    
    return render(request, 'signup/signup.html', {'form': form})