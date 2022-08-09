from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'music/head.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registr/register.html', {'user_form': user_form})


def log_on(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'music/head.html')
                else:
                    return render(request, 'registr/login.html', {'form': form})
            else:
                return render(request, 'registr/login.html', {'form': form})
    else:
        if request.user.is_authenticated:
            return redirect('head')
        else:
            form = LoginForm()
            return render(request, 'registr/login.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'music/head.html')
