from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('', views.login, name='signup'),
    path('admin/', include('adminpanel.urls'), name='adminpage'),
    path('user-page/', include('userpage.urls'), name='userpage'),
]
