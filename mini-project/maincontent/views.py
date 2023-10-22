from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import EmailSubscriptionForm

def home(request):
    return render(request, 'maincontent/home.html')


def about(request):
    form1 = EmailSubscriptionForm()
    form2 = EmailSubscriptionForm()
    return render(request, 'maincontent/about.html', {'form1': form1, 'form2': form2})

def contact(request):
    return render(request, 'maincontent/contact.html')

def email_submit(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')

        if form_id == 'form1':
            form = EmailSubscriptionForm(request.POST)
        elif form_id == 'form2':
            form = EmailSubscriptionForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            messages.success(request, f'Thank you for subscribing with email: {email} ({form_id.capitalize()})')
        else:
            messages.error(request, f'Form {form_id.capitalize()} is not valid.')

    form1 = EmailSubscriptionForm()
    form2 = EmailSubscriptionForm()

    return render(request, 'maincontent/about.html', {'form1': form1, 'form2': form2})
