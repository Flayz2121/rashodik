from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import  CustomUser
from .forms import LoginForm , users
from main.forms import KursyModelForm, PoSpiskuForm, NaLitsoForm, NaryadForm, BolnyeForm, UvolnenieForm, OtpuskForm
from main.models import  Kursy , bolnyes, naryads, uvolnenies, otpusks


def base_view(request, param1, param2 ):

    username = param1
    position = param2


            # Курсы инфо:
    kurses = Kursy.objects.all()
    catch_kurs = next((kurs for kurs in kurses if kurs.name_kurs == position), None)
    naryadss = naryads.objects.all()
    catch_naryad = next((naryad for naryad in naryadss if naryad.Kursy.name_kurs == position), None)
    bolens = bolnyes.objects.all()
    catch_bolen = next((bolen for bolen in bolens if bolen.Kursy.name_kurs == position), None)
    uvolneniess = uvolnenies.objects.all()
    catch_uvolnen = next((uvolnen for uvolnen in uvolneniess if uvolnen.Kursy.name_kurs == position), None)
    otpuskss = otpusks.objects.all()
    catch_otpusk = next((otpusk for otpusk in otpuskss if otpusk.Kursy.name_kurs == position), None)

    po_spisku_form = PoSpiskuForm(initial={'poSpisku': catch_kurs.poSpisku})
    na_litso_form = NaLitsoForm(initial={'naLitso': catch_kurs.naLitso})
    naryad_form = NaryadForm(initial={'naryad': catch_kurs.naryad})
    bolnye_form = BolnyeForm(initial={'bolnye': catch_kurs.bolnye})
    uvolnenie_form = UvolnenieForm(initial={'uvolnenie': catch_kurs.uvolnenie})
    otpusk_form = OtpuskForm(initial={'otpusk': catch_kurs.otpusk})

    if request.method == "POST":
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)

        # Обработка данных формы
        if po_spisku_form.is_valid():
            catch_kurs.poSpisku = po_spisku_form.cleaned_data['poSpisku']

        if na_litso_form.is_valid():
            catch_kurs.naLitso = na_litso_form.cleaned_data['naLitso']

        if naryad_form.is_valid():
            catch_kurs.naryad = naryad_form.cleaned_data['naryad']

        if bolnye_form.is_valid():
            catch_kurs.bolnye = bolnye_form.cleaned_data['bolnye']

        if uvolnenie_form.is_valid():
            catch_kurs.uvolnenie = uvolnenie_form.cleaned_data['uvolnenie']

        if otpusk_form.is_valid():
            catch_kurs.otpusk = otpusk_form.cleaned_data['otpusk']

        catch_kurs.save()


    context = {
            'username': username,
            'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
            'poSpisku': catch_kurs.poSpisku if catch_kurs else None,
            'naLitso': catch_kurs.naLitso if catch_kurs else None,
            'naryad': catch_kurs.naryad if catch_kurs else None,
            'bolnye': catch_kurs.bolnye if catch_kurs else None,
            'uvolnenie': catch_kurs.uvolnenie if catch_kurs else None,
            'otpusk': catch_kurs.otpusk if catch_kurs else None,
        #Формы:
            'po_spisku_form': po_spisku_form,
            'na_litso_form': na_litso_form,
            'naryad_form': naryad_form,
            'bolnye_form': bolnye_form,
            'uvolnenie_form': uvolnenie_form,
            'otpusk_form': otpusk_form,
        #Больные:
            'information_of_bolnyes': catch_bolen.information_of_bolnyes if catch_bolen else None,
            'information_of_bolnyes_2': catch_bolen.information_of_bolnyes_2 if catch_bolen else None,
            'information_of_bolnyes_3': catch_bolen.information_of_bolnyes_3 if catch_bolen else None,
            'information_of_bolnyes_4': catch_bolen.information_of_bolnyes_4 if catch_bolen else None,
            'information_of_bolnyes_5': catch_bolen.information_of_bolnyes_5 if catch_bolen else None,
            'information_of_bolnyes_6': catch_bolen.information_of_bolnyes_6 if catch_bolen else None,
            'information_of_bolnyes_7': catch_bolen.information_of_bolnyes_7 if catch_bolen else None,
            'information_of_bolnyes_8': catch_bolen.information_of_bolnyes_8 if catch_bolen else None,
            'information_of_bolnyes_9': catch_bolen.information_of_bolnyes_9 if catch_bolen else None,
            'information_of_bolnyes_10': catch_bolen.information_of_bolnyes_10 if catch_bolen else None,
            'information_of_bolnyes_11': catch_bolen.information_of_bolnyes_11 if catch_bolen else None,
            'information_of_bolnyes_12': catch_bolen.information_of_bolnyes_12 if catch_bolen else None,
            'information_of_bolnyes_13': catch_bolen.information_of_bolnyes_13 if catch_bolen else None,
            'information_of_bolnyes_14': catch_bolen.information_of_bolnyes_14 if catch_bolen else None,
            'information_of_bolnyes_15': catch_bolen.information_of_bolnyes_15 if catch_bolen else None,
            'information_of_bolnyes_16': catch_bolen.information_of_bolnyes_16 if catch_bolen else None,
            'information_of_bolnyes_17': catch_bolen.information_of_bolnyes_17 if catch_bolen else None,
            'information_of_bolnyes_18': catch_bolen.information_of_bolnyes_18 if catch_bolen else None,
            'information_of_bolnyes_19': catch_bolen.information_of_bolnyes_19 if catch_bolen else None,
            'information_of_bolnyes_20': catch_bolen.information_of_bolnyes_20 if catch_bolen else None,
            'information_of_bolnyes_21': catch_bolen.information_of_bolnyes_21 if catch_bolen else None,
            'information_of_bolnyes_22': catch_bolen.information_of_bolnyes_22 if catch_bolen else None,
            'information_of_bolnyes_23': catch_bolen.information_of_bolnyes_23 if catch_bolen else None,
            'information_of_bolnyes_24': catch_bolen.information_of_bolnyes_24 if catch_bolen else None,
            'information_of_bolnyes_25': catch_bolen.information_of_bolnyes_25 if catch_bolen else None,
            'information_of_bolnyes_26': catch_bolen.information_of_bolnyes_26 if catch_bolen else None,
            'information_of_bolnyes_27': catch_bolen.information_of_bolnyes_27 if catch_bolen else None,
            'information_of_bolnyes_28': catch_bolen.information_of_bolnyes_28 if catch_bolen else None,
            'information_of_bolnyes_29': catch_bolen.information_of_bolnyes_29 if catch_bolen else None,
            'information_of_bolnyes_30': catch_bolen.information_of_bolnyes_30 if catch_bolen else None,
            'information_of_bolnyes_31': catch_bolen.information_of_bolnyes_31 if catch_bolen else None,
            'information_of_bolnyes_32': catch_bolen.information_of_bolnyes_32 if catch_bolen else None,
            'information_of_bolnyes_33': catch_bolen.information_of_bolnyes_33 if catch_bolen else None,
            'information_of_bolnyes_34': catch_bolen.information_of_bolnyes_34 if catch_bolen else None,
            'information_of_bolnyes_35': catch_bolen.information_of_bolnyes_35 if catch_bolen else None,
            'information_of_bolnyes_36': catch_bolen.information_of_bolnyes_36 if catch_bolen else None,
            'information_of_bolnyes_37': catch_bolen.information_of_bolnyes_37 if catch_bolen else None,
            'information_of_bolnyes_38': catch_bolen.information_of_bolnyes_38 if catch_bolen else None,
            'information_of_bolnyes_39': catch_bolen.information_of_bolnyes_39 if catch_bolen else None,
            'information_of_bolnyes_40': catch_bolen.information_of_bolnyes_40 if catch_bolen else None,
        #Наряды
            'information_of_naryads': catch_naryad.information_of_naryads if catch_naryad else None,
            'information_of_naryads_2': catch_naryad.information_of_naryads_2 if catch_naryad else None,
            'information_of_naryads_3': catch_naryad.information_of_naryads_3 if catch_naryad else None,
            'information_of_naryads_4': catch_naryad.information_of_naryads_4 if catch_naryad else None,
            'information_of_naryads_5': catch_naryad.information_of_naryads_5 if catch_naryad else None,
            'information_of_naryads_6': catch_naryad.information_of_naryads_6 if catch_naryad else None,
            'information_of_naryads_7': catch_naryad.information_of_naryads_7 if catch_naryad else None,
            'information_of_naryads_8': catch_naryad.information_of_naryads_8 if catch_naryad else None,
            'information_of_naryads_9': catch_naryad.information_of_naryads_9 if catch_naryad else None,
            'information_of_naryads_10': catch_naryad.information_of_naryads_10 if catch_naryad else None,
            'information_of_naryads_11': catch_naryad.information_of_naryads_11 if catch_naryad else None,
            'information_of_naryads_12': catch_naryad.information_of_naryads_12 if catch_naryad else None,
            'information_of_naryads_13': catch_naryad.information_of_naryads_13 if catch_naryad else None,
            'information_of_naryads_14': catch_naryad.information_of_naryads_14 if catch_naryad else None,
            'information_of_naryads_15': catch_naryad.information_of_naryads_15 if catch_naryad else None,
            'information_of_naryads_16': catch_naryad.information_of_naryads_16 if catch_naryad else None,
            'information_of_naryads_17': catch_naryad.information_of_naryads_17 if catch_naryad else None,
            'information_of_naryads_18': catch_naryad.information_of_naryads_18 if catch_naryad else None,
            'information_of_naryads_19': catch_naryad.information_of_naryads_19 if catch_naryad else None,
            'information_of_naryads_20': catch_naryad.information_of_naryads_20 if catch_naryad else None,
            'information_of_naryads_21': catch_naryad.information_of_naryads_21 if catch_naryad else None,
            'information_of_naryads_22': catch_naryad.information_of_naryads_22 if catch_naryad else None,
            'information_of_naryads_23': catch_naryad.information_of_naryads_23 if catch_naryad else None,
            'information_of_naryads_24': catch_naryad.information_of_naryads_24 if catch_naryad else None,
            'information_of_naryads_25': catch_naryad.information_of_naryads_25 if catch_naryad else None,
            'information_of_naryads_26': catch_naryad.information_of_naryads_26 if catch_naryad else None,
            'information_of_naryads_27': catch_naryad.information_of_naryads_27 if catch_naryad else None,
            'information_of_naryads_28': catch_naryad.information_of_naryads_28 if catch_naryad else None,
            'information_of_naryads_29': catch_naryad.information_of_naryads_29 if catch_naryad else None,
            'information_of_naryads_30': catch_naryad.information_of_naryads_30 if catch_naryad else None,
            'information_of_naryads_31': catch_naryad.information_of_naryads_31 if catch_naryad else None,
            'information_of_naryads_32': catch_naryad.information_of_naryads_32 if catch_naryad else None,
            'information_of_naryads_33': catch_naryad.information_of_naryads_33 if catch_naryad else None,
            'information_of_naryads_34': catch_naryad.information_of_naryads_34 if catch_naryad else None,
            'information_of_naryads_35': catch_naryad.information_of_naryads_35 if catch_naryad else None,
            'information_of_naryads_36': catch_naryad.information_of_naryads_36 if catch_naryad else None,
            'information_of_naryads_37': catch_naryad.information_of_naryads_37 if catch_naryad else None,
            'information_of_naryads_38': catch_naryad.information_of_naryads_38 if catch_naryad else None,
            'information_of_naryads_39': catch_naryad.information_of_naryads_39 if catch_naryad else None,
            'information_of_naryads_40': catch_naryad.information_of_naryads_40 if catch_naryad else None,
        #Увольнения
            'information_of_uvolnenies': catch_uvolnen.information_of_uvolnenies if catch_uvolnen else None,
            'information_of_uvolnenies_2': catch_uvolnen.information_of_uvolnenies_2 if catch_uvolnen else None,
            'information_of_uvolnenies_3': catch_uvolnen.information_of_uvolnenies_3 if catch_uvolnen else None,
            'information_of_uvolnenies_4': catch_uvolnen.information_of_uvolnenies_4 if catch_uvolnen else None,
            'information_of_uvolnenies_5': catch_uvolnen.information_of_uvolnenies_5 if catch_uvolnen else None,
            'information_of_uvolnenies_6': catch_uvolnen.information_of_uvolnenies_6 if catch_uvolnen else None,
            'information_of_uvolnenies_7': catch_uvolnen.information_of_uvolnenies_7 if catch_uvolnen else None,
            'information_of_uvolnenies_8': catch_uvolnen.information_of_uvolnenies_8 if catch_uvolnen else None,
            'information_of_uvolnenies_9': catch_uvolnen.information_of_uvolnenies_9 if catch_uvolnen else None,
            'information_of_uvolnenies_10': catch_uvolnen.information_of_uvolnenies_10 if catch_uvolnen else None,
            'information_of_uvolnenies_11': catch_uvolnen.information_of_uvolnenies_11 if catch_uvolnen else None,
            'information_of_uvolnenies_12': catch_uvolnen.information_of_uvolnenies_12 if catch_uvolnen else None,
            'information_of_uvolnenies_13': catch_uvolnen.information_of_uvolnenies_13 if catch_uvolnen else None,
            'information_of_uvolnenies_14': catch_uvolnen.information_of_uvolnenies_14 if catch_uvolnen else None,
            'information_of_uvolnenies_15': catch_uvolnen.information_of_uvolnenies_15 if catch_uvolnen else None,
            'information_of_uvolnenies_16': catch_uvolnen.information_of_uvolnenies_16 if catch_uvolnen else None,
            'information_of_uvolnenies_17': catch_uvolnen.information_of_uvolnenies_17 if catch_uvolnen else None,
            'information_of_uvolnenies_18': catch_uvolnen.information_of_uvolnenies_18 if catch_uvolnen else None,
            'information_of_uvolnenies_19': catch_uvolnen.information_of_uvolnenies_19 if catch_uvolnen else None,
            'information_of_uvolnenies_20': catch_uvolnen.information_of_uvolnenies_20 if catch_uvolnen else None,
            'information_of_uvolnenies_21': catch_uvolnen.information_of_uvolnenies_21 if catch_uvolnen else None,
            'information_of_uvolnenies_22': catch_uvolnen.information_of_uvolnenies_22 if catch_uvolnen else None,
            'information_of_uvolnenies_23': catch_uvolnen.information_of_uvolnenies_23 if catch_uvolnen else None,
            'information_of_uvolnenies_24': catch_uvolnen.information_of_uvolnenies_24 if catch_uvolnen else None,
            'information_of_uvolnenies_25': catch_uvolnen.information_of_uvolnenies_25 if catch_uvolnen else None,
            'information_of_uvolnenies_26': catch_uvolnen.information_of_uvolnenies_26 if catch_uvolnen else None,
            'information_of_uvolnenies_27': catch_uvolnen.information_of_uvolnenies_27 if catch_uvolnen else None,
            'information_of_uvolnenies_28': catch_uvolnen.information_of_uvolnenies_28 if catch_uvolnen else None,
            'information_of_uvolnenies_29': catch_uvolnen.information_of_uvolnenies_29 if catch_uvolnen else None,
            'information_of_uvolnenies_30': catch_uvolnen.information_of_uvolnenies_30 if catch_uvolnen else None,
            'information_of_uvolnenies_31': catch_uvolnen.information_of_uvolnenies_31 if catch_uvolnen else None,
            'information_of_uvolnenies_32': catch_uvolnen.information_of_uvolnenies_32 if catch_uvolnen else None,
            'information_of_uvolnenies_33': catch_uvolnen.information_of_uvolnenies_33 if catch_uvolnen else None,
            'information_of_uvolnenies_34': catch_uvolnen.information_of_uvolnenies_34 if catch_uvolnen else None,
            'information_of_uvolnenies_35': catch_uvolnen.information_of_uvolnenies_35 if catch_uvolnen else None,
            'information_of_uvolnenies_36': catch_uvolnen.information_of_uvolnenies_36 if catch_uvolnen else None,
            'information_of_uvolnenies_37': catch_uvolnen.information_of_uvolnenies_37 if catch_uvolnen else None,
            'information_of_uvolnenies_38': catch_uvolnen.information_of_uvolnenies_38 if catch_uvolnen else None,
            'information_of_uvolnenies_39': catch_uvolnen.information_of_uvolnenies_39 if catch_uvolnen else None,
            'information_of_uvolnenies_40': catch_uvolnen.information_of_uvolnenies_40 if catch_uvolnen else None,
        #Отпуск
            'information_of_otpusks': catch_otpusk.information_of_otpusks if catch_otpusk else None,
            'information_of_otpusks_2': catch_otpusk.information_of_otpusks_2 if catch_otpusk else None,
            'information_of_otpusks_3': catch_otpusk.information_of_otpusks_3 if catch_otpusk else None,
            'information_of_otpusks_4': catch_otpusk.information_of_otpusks_4 if catch_otpusk else None,
            'information_of_otpusks_5': catch_otpusk.information_of_otpusks_5 if catch_otpusk else None,
            'information_of_otpusks_6': catch_otpusk.information_of_otpusks_6 if catch_otpusk else None,
            'information_of_otpusks_7': catch_otpusk.information_of_otpusks_7 if catch_otpusk else None,
            'information_of_otpusks_8': catch_otpusk.information_of_otpusks_8 if catch_otpusk else None,
            'information_of_otpusks_9': catch_otpusk.information_of_otpusks_9 if catch_otpusk else None,
            'information_of_otpusks_10': catch_otpusk.information_of_otpusks_10 if catch_otpusk else None,
            'information_of_otpusks_11': catch_otpusk.information_of_otpusks_11 if catch_otpusk else None,
            'information_of_otpusks_12': catch_otpusk.information_of_otpusks_12 if catch_otpusk else None,
            'information_of_otpusks_13': catch_otpusk.information_of_otpusks_13 if catch_otpusk else None,
            'information_of_otpusks_14': catch_otpusk.information_of_otpusks_14 if catch_otpusk else None,
            'information_of_otpusks_15': catch_otpusk.information_of_otpusks_15 if catch_otpusk else None,
            'information_of_otpusks_16': catch_otpusk.information_of_otpusks_16 if catch_otpusk else None,
            'information_of_otpusks_17': catch_otpusk.information_of_otpusks_17 if catch_otpusk else None,
            'information_of_otpusks_18': catch_otpusk.information_of_otpusks_18 if catch_otpusk else None,
            'information_of_otpusks_19': catch_otpusk.information_of_otpusks_19 if catch_otpusk else None,
            'information_of_otpusks_20': catch_otpusk.information_of_otpusks_20 if catch_otpusk else None,
            'information_of_otpusks_21': catch_otpusk.information_of_otpusks_21 if catch_otpusk else None,
            'information_of_otpusks_22': catch_otpusk.information_of_otpusks_22 if catch_otpusk else None,
            'information_of_otpusks_23': catch_otpusk.information_of_otpusks_23 if catch_otpusk else None,
            'information_of_otpusks_24': catch_otpusk.information_of_otpusks_24 if catch_otpusk else None,
            'information_of_otpusks_25': catch_otpusk.information_of_otpusks_25 if catch_otpusk else None,
            'information_of_otpusks_26': catch_otpusk.information_of_otpusks_26 if catch_otpusk else None,
            'information_of_otpusks_27': catch_otpusk.information_of_otpusks_27 if catch_otpusk else None,
            'information_of_otpusks_28': catch_otpusk.information_of_otpusks_28 if catch_otpusk else None,
            'information_of_otpusks_29': catch_otpusk.information_of_otpusks_29 if catch_otpusk else None,
            'information_of_otpusks_30': catch_otpusk.information_of_otpusks_30 if catch_otpusk else None,
            'information_of_otpusks_31': catch_otpusk.information_of_otpusks_31 if catch_otpusk else None,
            'information_of_otpusks_32': catch_otpusk.information_of_otpusks_32 if catch_otpusk else None,
            'information_of_otpusks_33': catch_otpusk.information_of_otpusks_33 if catch_otpusk else None,
            'information_of_otpusks_34': catch_otpusk.information_of_otpusks_34 if catch_otpusk else None,
            'information_of_otpusks_35': catch_otpusk.information_of_otpusks_35 if catch_otpusk else None,
            'information_of_otpusks_36': catch_otpusk.information_of_otpusks_36 if catch_otpusk else None,
            'information_of_otpusks_37': catch_otpusk.information_of_otpusks_37 if catch_otpusk else None,
            'information_of_otpusks_38': catch_otpusk.information_of_otpusks_38 if catch_otpusk else None,
            'information_of_otpusks_39': catch_otpusk.information_of_otpusks_39 if catch_otpusk else None,
            'information_of_otpusks_40': catch_otpusk.information_of_otpusks_40 if catch_otpusk else None,

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

