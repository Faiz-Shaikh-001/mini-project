from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('email-submit/form1/', views.email_submit, name='email-submit1'),
    path('email-submit/form2/', views.email_submit, name='email-submit2'),
]


