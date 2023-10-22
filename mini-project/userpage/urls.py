from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_page, name='user-page'),  # Define a name for the user_page URL
    path('user/profile', views.user_profile, name='user-profile'),
    path('user/bookdetail', views.book_detail, name='book-detail'),
]
