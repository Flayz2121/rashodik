from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from authin import forms
from .models import  CustomUser
from .forms import LoginForm, users
from main.models import  Kursy


def base_view(request, param1, param2 ):

    username = param1
    position = param2


            # Курсы инфо:
    kurses = Kursy.objects.all()
    catch_kurs = next((kurs for kurs in kurses if kurs.name_kurs == position), None)

    context = {
            'username': username,
            'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
            'poSpisku': catch_kurs.poSpisku if catch_kurs else None,
            'naLitso': catch_kurs.naLitso if catch_kurs else None,
            'naryad': catch_kurs.naryad if catch_kurs else None,
            'bolnye': catch_kurs.bolnye if catch_kurs else None,
            'uvolnenie': catch_kurs.uvolnenie if catch_kurs else None,
            'otpusk': catch_kurs.otpusk if catch_kurs else None
    }
    return render(request, 'base.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['selection']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.get(id=username)
                user = authenticate(username=user.username, password=password)

                if user is not None:
                    login(request, user)
                    username = user.username
                    position = user.position
                    redirect_params = {
                        'param1': username,
                        'param2': position
                    }
                    return redirect('base',**redirect_params)
                else:
                    err = True
                    context = {
                        'err': err,
                        'form': form
                    }
                return render(request, 'login.html', context)
            except CustomUser.DoesNotExist:
                form.add_error('selection', "Пользователь не найден")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

