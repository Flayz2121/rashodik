from .models import Kursy, naryads, bolnyes, uvolnenies, otpusks
from authin.models import CustomUser
from django.shortcuts import render, redirect
from .forms import bolnyesModelForm, naryadsModelForm, uvolneniesModelForm, otpusksModelForm, PoSpiskuForm, NaLitsoForm, NaryadForm, BolnyeForm, UvolnenieForm, OtpuskForm, naryadsMestoModelForm, naryadsVremyaModelForm, bolnyesMestoModelForm, bolnyesVremyaModelForm,  uvolneniesMestoModelForm, uvolneniesVremyaModelForm, otpusksMestoModelForm, otpusksVremyaModelForm

def edit_naryad(request, param1, param3):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1
    a = param3

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
    form_naryads_mesto = naryadsMestoModelForm(instance=catch_naryad)
    form_naryads_vremya = naryadsVremyaModelForm(instance=catch_naryad)

    if request.method == "POST":
        # Формы нарядов: Фамилия, Место, Время.
        form_naryads = naryadsModelForm(request.POST, instance=catch_naryad)
        form_naryads_mesto = naryadsMestoModelForm(request.POST, instance=catch_naryad)
        form_naryads_vremya = naryadsVremyaModelForm(request.POST, instance=catch_naryad)
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_naryads.is_valid():
            form_naryads.save()

        if form_naryads_mesto.is_valid():
            form_naryads_mesto.save()

        if form_naryads_vremya.is_valid():
            form_naryads_vremya.save()

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
        'form_naryads_mesto':form_naryads_mesto,
        'form_naryads_vremya':form_naryads_vremya,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        #Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
        'a':a,

    }

    return render(request, "edit_naryad.html", context)

def edit_uvolnenie(request, param1, param3):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1
    a = param3


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
    form_uvolnenies_mesto = uvolneniesMestoModelForm(instance=catch_uvolnen)
    form_uvolnenies_vremya = uvolneniesVremyaModelForm(instance=catch_uvolnen)


    if request.method == "POST":
        # Формы увольнения: Фамилия, Место, Время.
        form_uvolnenies = uvolneniesModelForm(request.POST, instance=catch_uvolnen)
        form_uvolnenies_mesto = uvolneniesMestoModelForm(request.POST,instance=catch_uvolnen)
        form_uvolnenies_vremya = uvolneniesVremyaModelForm(request.POST,instance=catch_uvolnen)

        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_uvolnenies.is_valid():
            form_uvolnenies.save()

        if form_uvolnenies_mesto.is_valid():
            form_uvolnenies_mesto.save()

        if form_uvolnenies_vremya.is_valid():
            form_uvolnenies_vremya.save()

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
        'form_uvolnenies_mesto':form_uvolnenies_mesto,
        'form_uvolnenies_vremya':form_uvolnenies_vremya,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        # Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
        'a': a,

    }

    return render(request, "edit_uvolnenie.html", context)

def edit_bolen(request, param1, param3):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1
    a = param3

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
    form_bolnyes_mesto = bolnyesMestoModelForm(instance=catch_bolen)
    form_bolnyes_vremya = bolnyesVremyaModelForm(instance=catch_bolen)

    if request.method == "POST":
        #Формы больных: Фамилия, Место, Время.
        form_bolnyes = bolnyesModelForm(request.POST,instance=catch_bolen)
        form_bolnyes_mesto = bolnyesMestoModelForm(request.POST,instance=catch_bolen)
        form_bolnyes_vremya = bolnyesVremyaModelForm(request.POST,instance=catch_bolen)

        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_bolnyes.is_valid():
            form_bolnyes.save()

        if form_bolnyes_mesto.is_valid():
            form_bolnyes_mesto.save()

        if form_bolnyes_vremya.is_valid():
            form_bolnyes_vremya.save()

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
        'form_bolnyes_mesto':form_bolnyes_mesto,
        'form_bolnyes_vremya':form_bolnyes_vremya,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        # Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
        'a': a,
    }
    return render(request, "edit_bolen.html", context)

def edit_otpusk(request, param1, param3):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1
    a = param3

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
    form_otpusks_mesto = otpusksMestoModelForm(instance=catch_otpusk)
    form_otpusks_vremya = otpusksVremyaModelForm(instance=catch_otpusk)


    if request.method == "POST":
        #Формы отпуска: Фамилия, Место, Время.
        form_otpusks = otpusksModelForm(request.POST, instance=catch_otpusk)
        form_otpusks_mesto = otpusksMestoModelForm(request.POST, instance=catch_otpusk)
        form_otpusks_vremya = otpusksVremyaModelForm(request.POST, instance=catch_otpusk)
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)
        if form_otpusks.is_valid():
            form_otpusks.save()

        if form_otpusks_mesto.is_valid():
            form_otpusks_mesto.save()

        if form_otpusks_vremya.is_valid():
            form_otpusks_vremya.save()

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
        'form_otpusks_vremya':form_otpusks_vremya,
        'form_otpusks_mesto':form_otpusks_mesto,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        # Формы:
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
        'a': a,
    }
    return render(request, "edit_otpusk.html", context)

def make_kursants(request, param1, param3):
    catch_kurs = Kursy.objects.get(name_kurs=param1)
    user = CustomUser.objects.get(position=param1)
    username = user.username
    position = param1
    a = param3

    po_spisku_form = PoSpiskuForm(initial={'poSpisku': catch_kurs.poSpisku})
    na_litso_form = NaLitsoForm(initial={'naLitso': catch_kurs.naLitso})
    naryad_form = NaryadForm(initial={'naryad': catch_kurs.naryad})
    bolnye_form = BolnyeForm(initial={'bolnye': catch_kurs.bolnye})
    uvolnenie_form = UvolnenieForm(initial={'uvolnenie': catch_kurs.uvolnenie})
    otpusk_form = OtpuskForm(initial={'otpusk': catch_kurs.otpusk})

    if request.method == "POST":
        #Формы расходов:
        po_spisku_form = PoSpiskuForm(request.POST)
        na_litso_form = NaLitsoForm(request.POST)
        naryad_form = NaryadForm(request.POST)
        bolnye_form = BolnyeForm(request.POST)
        uvolnenie_form = UvolnenieForm(request.POST)
        otpusk_form = OtpuskForm(request.POST)

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
        'username':username,
        'position':position,
        'a':a,
        'name_kurs': catch_kurs.name_kurs if catch_kurs else None,
        'po_spisku_form': po_spisku_form,
        'na_litso_form': na_litso_form,
        'naryad_form': naryad_form,
        'bolnye_form': bolnye_form,
        'uvolnenie_form': uvolnenie_form,
        'otpusk_form': otpusk_form,
    }
    return render (request, "make_kursants.html", context)


def fakultet(request, param1, param2):
    username = param1
    position = param2

    # Получаем все курсы, относящиеся к факультету
    all_fakultet_objects = Kursy.objects.filter(fakultet=position).order_by('name_kurs')

    fakultets = []
    kafedras = []
    kursy_list = []

    all_kursy_data = []

    for kurs in all_fakultet_objects:
        kurs_name = kurs.name_kurs

        # Определяем уровень: факультет, кафедра или курс
        if "факультет" in kurs_name.lower():
            fakultets.append(kurs)
            a = 0  # Флаг, скрывающий поле "увольнение" для факультетов и кафедр
        elif "кафедра" in kurs_name.lower():
            kafedras.append(kurs)
            a = 0
        else:
            kursy_list.append(kurs)
            a = 1

        kurs_data = {
            'kurs_name': kurs_name,
            'naryads': [],
            'bolnyes': [],
            'uvolnenies': [],
            'otpusks': [],
            'rashod': {
                'poSpisku': kurs.poSpisku if kurs else None,
                'naLitso': kurs.naLitso if kurs else None,
                'naryad': kurs.naryad if kurs else None,
                'bolnye': kurs.bolnye if kurs else None,
                'uvolnenie': kurs.uvolnenie if kurs else None,
                'otpusk': kurs.otpusk if kurs else None,
            },
            'a': a,  # Показывать или нет "курс"
        }

        # Заполняем данные о нарядах
        naryad_object = naryads.objects.filter(Kursy_id=kurs_name).first()
        if naryad_object:
            for i in range(1, 41):
                name = getattr(naryad_object, f'information_of_naryads_{i}', None)
                place = getattr(naryad_object, f'info_of_naryads_{i}_mesto', None)
                time = getattr(naryad_object, f'info_of_naryads_{i}_vremya', None)
                if name and place and time:
                    kurs_data['naryads'].append((name, place, time))

        # Заполняем данные о больных
        bolnye_object = bolnyes.objects.filter(Kursy_id=kurs_name).first()
        if bolnye_object:
            for i in range(1, 41):
                name = getattr(bolnye_object, f'information_of_bolnyes_{i}', None)
                place = getattr(bolnye_object, f'info_of_bolnyes_{i}_mesto', None)
                time = getattr(bolnye_object, f'info_of_bolnyes_{i}_vremya', None)
                if name and place and time:
                    kurs_data['bolnyes'].append((name, place, time))

        # Заполняем данные об увольнениях
        uvolnenie_object = uvolnenies.objects.filter(Kursy_id=kurs_name).first()
        if uvolnenie_object:
            for i in range(1, 41):
                name = getattr(uvolnenie_object, f'information_of_uvolnenies_{i}', None)
                place = getattr(uvolnenie_object, f'info_of_uvolnenies_{i}_mesto', None)
                time = getattr(uvolnenie_object, f'info_of_uvolnenies_{i}_vremya', None)
                if name and place and time:
                    kurs_data['uvolnenies'].append((name, place, time))

        # Заполняем данные об отпусках
        otpusk_object = otpusks.objects.filter(Kursy_id=kurs_name).first()
        if otpusk_object:
            for i in range(1, 41):
                name = getattr(otpusk_object, f'information_of_otpusks_{i}', None)
                place = getattr(otpusk_object, f'info_of_otpusks_{i}_mesto', None)
                time = getattr(otpusk_object, f'info_of_otpusks_{i}_vremya', None)
                if name and place and time:
                    kurs_data['otpusks'].append((name, place, time))

        all_kursy_data.append(kurs_data)

    # Сортировка: факультеты → кафедры → курсы
    sorted_kursy_data = sorted(all_kursy_data, key=lambda x: (x['a'], x['kurs_name']))

    context = {
        'username': username,
        'position': position,
        'fakultets': fakultets,
        'kafedras': kafedras,
        'kursy_list': kursy_list,
        'all_kursy_data': sorted_kursy_data,
    }
    return render(request, 'fakultet.html', context)

def fakultet_all(request, param1, param2):
    username = param1
    position = param2

    # Получаем все данные курсов
    all_kursy_data = Kursy.objects.all()

    # Собираем данные для сводной таблицы
    сводные_данные = []

    for kurs_data in all_kursy_data:

        # Добавляем данные о нарядах
        for naryad in kurs_data.naryads.all():
            for i in range(1, 41):
                name = getattr(naryad, f'information_of_naryads_{i}', None)
                place = getattr(naryad, f'info_of_naryads_{i}_mesto', None)
                time = getattr(naryad, f'info_of_naryads_{i}_vremya', None)
                if name and place and time:
                    сводные_данные.append({
                        'kurs_name': kurs_data.name_kurs,
                        'name': name,
                        'status': 'Наряд',
                        'place': place,
                        'time': time,
                    })

        # Добавляем данные о больных
        for bolnye in kurs_data.bolnyes.all():
            for i in range(1, 41):
                name = getattr(bolnye, f'information_of_bolnyes_{i}', None)
                place = getattr(bolnye, f'info_of_bolnyes_{i}_mesto', None)
                time = getattr(bolnye, f'info_of_bolnyes_{i}_vremya', None)
                if name and place and time:
                    сводные_данные.append({
                        'kurs_name': kurs_data.name_kurs,
                        'name': name,
                        'status': 'Болен',
                        'place': place,
                        'time': time,
                    })

        # Добавляем данные об увольнениях
        for uvolnenie in kurs_data.uvolnenies.all():
            for i in range(1, 41):
                name = getattr(uvolnenie, f'information_of_uvolnenies_{i}', None)
                place = getattr(uvolnenie, f'info_of_uvolnenies_{i}_mesto', None)
                time = getattr(uvolnenie, f'info_of_uvolnenies_{i}_vremya', None)
                if name and place and time:
                    сводные_данные.append({
                        'kurs_name': kurs_data.name_kurs,
                        'name': name,
                        'status': 'Увольнение',
                        'place': place,
                        'time': time,
                    })

        # Добавляем данные об отпусках
        for otpusk in kurs_data.otpusks.all():
            for i in range(1, 41):
                name = getattr(otpusk, f'information_of_otpusks_{i}', None)
                place = getattr(otpusk, f'info_of_otpusks_{i}_mesto', None)
                time = getattr(otpusk, f'info_of_otpusks_{i}_vremya', None)
                if name and place and time:
                    сводные_данные.append({
                        'kurs_name': kurs_data.name_kurs,
                        'name': name,
                        'status': 'Отпуск',
                        'place': place,
                        'time': time,
                    })



    # Передаем данные в шаблон
    context = {
        'username': username,
        'position': position,
        'сводные_данные': сводные_данные,
    }

    return render(request, 'fakultet_all.html', context)