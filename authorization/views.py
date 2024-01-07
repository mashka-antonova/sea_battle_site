from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def logout_view(request):
    logout(request)
    return redirect('main')  # Перенаправление на главную страницу после выхода


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('main')  # Перенаправление на главную страницу после входа
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('main')  # Перенаправление на главную страницу после регистрации
    else:
        form = UserCreationForm()

    return render(request, 'auth/register_form.html', {'form': form})
