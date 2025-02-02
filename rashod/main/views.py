from .models import Kursy, naryads, bolnyes, uvolnenies, otpusks
from authin.models import CustomUser
from django.shortcuts import render, redirect
from .forms import bolnyesModelForm, naryadsModelForm, uvolneniesModelForm, otpusksModelForm, PoSpiskuForm, NaLitsoForm, NaryadForm, BolnyeForm, UvolnenieForm, OtpuskForm

def edit_naryad(request, param1):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1

    naryadss = naryads.objects.all()
    catch_naryad = next((naryad for naryad in naryadss if naryad.Kursy.name_kurs == position), None)

    po_spisku_form = PoSpiskuForm(initial={'poSpisku': catch_kurs.poSpisku})
    na_litso_form = NaLitsoForm(initial={'naLitso': catch_kurs.naLitso})
    naryad_form = NaryadForm(initial={'naryad': catch_kurs.naryad})
    bolnye_form = BolnyeForm(initial={'bolnye': catch_kurs.bolnye})
    uvolnenie_form = UvolnenieForm(initial={'uvolnenie': catch_kurs.uvolnenie})
    otpusk_form = OtpuskForm(initial={'otpusk': catch_kurs.otpusk})

    #форма нарядов
    form_naryads = naryadsModelForm(instance=catch_naryad)

    if request.method == "POST":
        form_naryads = naryadsModelForm(request.POST, instance=catch_naryad)
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_naryads.is_valid():
            form_naryads.save()

        if po_spisku_form.is_valid():
            catch_kurs.poSpisku = po_spisku_form.cleaned_data['poSpisku']
            catch_kurs.save()
        if na_litso_form.is_valid():
            catch_kurs.naLitso = na_litso_form.cleaned_data['naLitso']
            catch_kurs.save()
        if naryad_form.is_valid():
            catch_kurs.naryad = naryad_form.cleaned_data['naryad']
            catch_kurs.save()
        if bolnye_form.is_valid():
            catch_kurs.bolnye = bolnye_form.cleaned_data['bolnye']
            catch_kurs.save()
        if uvolnenie_form.is_valid():
            catch_kurs.uvolnenie = uvolnenie_form.cleaned_data['uvolnenie']
            catch_kurs.save()
        if otpusk_form.is_valid():
            catch_kurs.otpusk = otpusk_form.cleaned_data['otpusk']
            catch_kurs.save()


    context = {
        'position':position,
        'username': username,
        'form_naryads': form_naryads,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        #Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,

    }

    return render(request, "edit_naryad.html", context)

def edit_uvolnenie(request, param1):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1

    uvolneniess = uvolnenies.objects.all()
    catch_uvolnen = next((uvolnen for uvolnen in uvolneniess if uvolnen.Kursy.name_kurs == position), None)

    po_spisku_form = PoSpiskuForm(initial={'poSpisku': catch_kurs.poSpisku})
    na_litso_form = NaLitsoForm(initial={'naLitso': catch_kurs.naLitso})
    naryad_form = NaryadForm(initial={'naryad': catch_kurs.naryad})
    bolnye_form = BolnyeForm(initial={'bolnye': catch_kurs.bolnye})
    uvolnenie_form = UvolnenieForm(initial={'uvolnenie': catch_kurs.uvolnenie})
    otpusk_form = OtpuskForm(initial={'otpusk': catch_kurs.otpusk})

    #форма увольнения
    form_uvolnenies = uvolneniesModelForm(instance=catch_uvolnen)


    if request.method == "POST":
        form_uvolnenies = uvolneniesModelForm(request.POST, instance=catch_uvolnen)
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_uvolnenies.is_valid():
            form_uvolnenies.save()

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
        'position':position,
        'username': username,
        'form_uvolnenies': form_uvolnenies,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        # Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
    }

    return render(request, "edit_uvolnenie.html", context)

def edit_bolen(request, param1):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1

    bolens = bolnyes.objects.all()
    catch_bolen = next((bolen for bolen in bolens if bolen.Kursy.name_kurs == position), None)

    po_spisku_form = PoSpiskuForm(initial={'poSpisku': catch_kurs.poSpisku})
    na_litso_form = NaLitsoForm(initial={'naLitso': catch_kurs.naLitso})
    naryad_form = NaryadForm(initial={'naryad': catch_kurs.naryad})
    bolnye_form = BolnyeForm(initial={'bolnye': catch_kurs.bolnye})
    uvolnenie_form = UvolnenieForm(initial={'uvolnenie': catch_kurs.uvolnenie})
    otpusk_form = OtpuskForm(initial={'otpusk': catch_kurs.otpusk})

    #форма больных
    form_bolnyes = bolnyesModelForm(instance=catch_bolen)


    if request.method == "POST":
        form_bolnyes = bolnyesModelForm(request.POST,instance=catch_bolen)
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_bolnyes.is_valid():
            form_bolnyes.save()

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
        'position':position,
        'username': username,
        'form_bolnyes': form_bolnyes,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        # Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
    }
    return render(request, "edit_bolen.html", context)

def edit_otpusk(request, param1):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1

    otpuskss = otpusks.objects.all()
    catch_otpusk = next((otpusk for otpusk in otpuskss if otpusk.Kursy.name_kurs == position), None)

    po_spisku_form = PoSpiskuForm(initial={'poSpisku': catch_kurs.poSpisku})
    na_litso_form = NaLitsoForm(initial={'naLitso': catch_kurs.naLitso})
    naryad_form = NaryadForm(initial={'naryad': catch_kurs.naryad})
    bolnye_form = BolnyeForm(initial={'bolnye': catch_kurs.bolnye})
    uvolnenie_form = UvolnenieForm(initial={'uvolnenie': catch_kurs.uvolnenie})
    otpusk_form = OtpuskForm(initial={'otpusk': catch_kurs.otpusk})

    #форма отпуска
    form_otpusks = otpusksModelForm(instance=catch_otpusk)


    if request.method == "POST":
        form_otpusks = otpusksModelForm(request.POST, instance=catch_otpusk)
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_otpusks.is_valid():
            form_otpusks.save()

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
        'position':position,
        'username': username,
        'form_otpusks': form_otpusks,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        # Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
    }
    return render(request, "edit_otpusk.html", context)
