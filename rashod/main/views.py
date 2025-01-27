from .models import Kursy
from authin.models import CustomUser
from django.shortcuts import render, redirect
from .forms import KursyModelForm

def edit(request, param1):
    try:
        catch_kurs = Kursy.objects.get(name_kurs=param1)
    except Kursy.DoesNotExist:
        context = {'error': 'Объект не найден'}
        return render(request, "edit.html", context)

    user = CustomUser.objects.get(position=param1)
    username = user.username

    form = KursyModelForm(instance=catch_kurs)

    if request.method == "POST":
        form = KursyModelForm(request.POST, instance=catch_kurs)

        if form.is_valid():
            form.save()

            position = param1
            redirect_params = {
                'param1': username,
                'param2': position,
            }
            return redirect('base',**redirect_params)

    context = {
        'username': username,
        'form': form,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        'poSpisku': catch_kurs.poSpisku if catch_kurs else None,
        'naLitso': catch_kurs.naLitso if catch_kurs else None,
        'naryad': catch_kurs.naryad if catch_kurs else None,
        'bolnye': catch_kurs.bolnye if catch_kurs else None,
        'uvolnenie': catch_kurs.uvolnenie if catch_kurs else None,
        'otpusk': catch_kurs.otpusk if catch_kurs else None
    }

    return render(request, "edit.html", context)
