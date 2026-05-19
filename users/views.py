from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        username     = request.POST['username']
        password     = request.POST['password']
        phone        = request.POST['phone']
        neighborhood = request.POST['neighborhood']
        city         = request.POST['city']
        avatar       = request.FILES.get('avatar')

        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(
            user         = user,
            phone        = phone,
            neighborhood = neighborhood,
            city         = city,
            avatar       = avatar,
        )
        login(request, user)
        return redirect('item-list')

    return render(request, 'users/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('item-list')
        else:
            return render(request, 'users/login.html', {'error': 'اسم المستخدم أو كلمة المرور خاطئة'})

    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')