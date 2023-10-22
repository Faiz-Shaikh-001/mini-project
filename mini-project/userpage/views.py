from django.shortcuts import render

def user_page(request):
    return render(request, 'userpage/user-page.html')


def user_profile(request):
    return render(request, 'userpage/profiile.html')


def book_detail(request):
    return render(request, 'userpage/book-detail.html')