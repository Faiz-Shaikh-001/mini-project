from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('admin/', include('adminpanel.urls'), name='adminpage'),
    path('user-page/', include('userpage.urls'), name='userpage'),
]
