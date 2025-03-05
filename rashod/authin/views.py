from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import  CustomUser
from .forms import LoginForm
from main.forms import KursyModelForm, PoSpiskuForm, NaLitsoForm, NaryadForm, BolnyeForm, UvolnenieForm, OtpuskForm
from main.models import  Kursy , bolnyes, naryads, uvolnenies, otpusks
import json


def base_view(request, param1, param2 ):
    username = param1
    position = param2

    #Переменная для изменеия расхода дежурным по факу или начальником факультета
    user = CustomUser.objects.get(username=username)
    position_dezha = user.position
    if  position_dezha != position:
        b = 1
    else:
        b = 0


    #факультеты:
    if position == '1' or position == '2' or position == '3' or position == '4' or position == '5' or position == '6'\
            or position == '7' or position == '8' or position == '9' or position == 'СПЕЦФАК' or position == 'СПО':#11-СПО
        redirect_params = {
                'param1': username,
                'param2': position
                }
        return redirect('fakultet',**redirect_params)

    # Курсы инфо:
    kurses = Kursy.objects.all()
    catch_kurs = next((kurs for kurs in kurses if kurs.name_kurs == position), None)

    # Определение форм
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

    # Переменная отвечающая за не вывод поля увольнения для кафедр, и редактирующая факультетскую html
    if catch_kurs.name_kurs == '11 кафедра' or catch_kurs.name_kurs == '12 кафедра' or catch_kurs.name_kurs == '13 кафедра' or catch_kurs.name_kurs == '14 кафедра' \
            or catch_kurs.name_kurs == '15 кафедра' or catch_kurs.name_kurs == '16 кафедра':
        a = 0
    else:
        a = 1


#Наряды
    try:
            object = naryads.objects.get(Kursy_id=catch_kurs.name_kurs)
    except naryads.DoesNotExist:
            # Обработка случая, если объект не найден
            object = None
    except naryads.MultipleObjectsReturned:
            # Обработка случая, если найдено несколько объектов
            object = None
    if object:
            table_data = {
                    'Имя': [],
                    'Место': [],
                    'Время': []
            }
            # Генерация списков на основе полей объекта
            for i in range(1, 41):
                    table_data['Имя'].append(getattr(object, f'information_of_naryads_{i}', None))
                    table_data['Место'].append(getattr(object, f'info_of_naryads_{i}_mesto', None))
                    table_data['Время'].append(getattr(object, f'info_of_naryads_{i}_vremya', None))
            # Удаляем пустые значения (если поля не заполнены)
            table_data['Имя'] = [x for x in table_data['Имя'] if x is not None]
            table_data['Место'] = [x for x in table_data['Место'] if x is not None]
            table_data['Время'] = [x for x in table_data['Время'] if x is not None]
            # Создаем zip-объект
            zipped_data_naryads = zip(table_data['Имя'], table_data['Место'], table_data['Время'])
    else:
            zipped_data_naryads = []
############################################

#Больные
    try:
            object = bolnyes.objects.get(Kursy_id=catch_kurs.name_kurs)
    except naryads.DoesNotExist:
            # Обработка случая, если объект не найден
            object = None
    except naryads.MultipleObjectsReturned:
            # Обработка случая, если найдено несколько объектов
            object = None
    if object:
            table_data = {
                    'Имя': [],
                    'Место': [],
                    'Время': []
            }
            # Генерация списков на основе полей объекта
            for i in range(1, 41):
                    table_data['Имя'].append(getattr(object, f'information_of_bolnyes_{i}', None))
                    table_data['Место'].append(getattr(object, f'info_of_bolnyes_{i}_mesto', None))
                    table_data['Время'].append(getattr(object, f'info_of_bolnyes_{i}_vremya', None))
            # Удаляем пустые значения (если поля не заполнены)
            table_data['Имя'] = [x for x in table_data['Имя'] if x is not None]
            table_data['Место'] = [x for x in table_data['Место'] if x is not None]
            table_data['Время'] = [x for x in table_data['Время'] if x is not None]
            # Создаем zip-объект
            zipped_data_bolnyes = zip(table_data['Имя'], table_data['Место'], table_data['Время'])
    else:
            zipped_data_bolnyes = []
############################################

#Увольнение
    try:
            object = uvolnenies.objects.get(Kursy_id=catch_kurs.name_kurs)
    except naryads.DoesNotExist:
            # Обработка случая, если объект не найден
            object = None
    except naryads.MultipleObjectsReturned:
            # Обработка случая, если найдено несколько объектов
            object = None
    if object:
            table_data = {
                    'Имя': [],
                    'Место': [],
                    'Время': []
            }
            # Генерация списков на основе полей объекта
            for i in range(1, 41):
                    table_data['Имя'].append(getattr(object, f'information_of_uvolnenies_{i}', None))
                    table_data['Место'].append(getattr(object, f'info_of_uvolnenies_{i}_mesto', None))
                    table_data['Время'].append(getattr(object, f'info_of_uvolnenies_{i}_vremya', None))
            # Удаляем пустые значения (если поля не заполнены)
            table_data['Имя'] = [x for x in table_data['Имя'] if x is not None]
            table_data['Место'] = [x for x in table_data['Место'] if x is not None]
            table_data['Время'] = [x for x in table_data['Время'] if x is not None]
            # Создаем zip-объект
            zipped_data_uvolnenies = zip(table_data['Имя'], table_data['Место'], table_data['Время'])
    else:
            zipped_data_uvolnenies = []
############################################

#Отпуска
    try:
            object = otpusks.objects.get(Kursy_id=catch_kurs.name_kurs)
    except naryads.DoesNotExist:
            # Обработка случая, если объект не найден
            object = None
    except naryads.MultipleObjectsReturned:
            # Обработка случая, если найдено несколько объектов
            object = None
    if object:
            table_data = {
                    'Имя': [],
                    'Место': [],
                    'Время': []
            }
            # Генерация списков на основе полей объекта
            for i in range(1, 41):
                    table_data['Имя'].append(getattr(object, f'information_of_otpusks_{i}', None))
                    table_data['Место'].append(getattr(object, f'info_of_otpusks_{i}_mesto', None))
                    table_data['Время'].append(getattr(object, f'info_of_otpusks_{i}_vremya', None))
            # Удаляем пустые значения (если поля не заполнены)
            table_data['Имя'] = [x for x in table_data['Имя'] if x is not None]
            table_data['Место'] = [x for x in table_data['Место'] if x is not None]
            table_data['Время'] = [x for x in table_data['Время'] if x is not None]
            # Создаем zip-объект
            zipped_data_otpusks = zip(table_data['Имя'], table_data['Место'], table_data['Время'])
    else:
            zipped_data_otpusks = []
############################################

    context = {
        #для таблиц расхода курсов/кафедр
            'zipped_data_naryads':zipped_data_naryads,
            'zipped_data_bolnyes': zipped_data_bolnyes,
            'zipped_data_uvolnenies':zipped_data_uvolnenies,
            'zipped_data_otpusks':zipped_data_otpusks,
        #Переменная для не вывода поля "увольнения" для кафедры
            'position_dezha':position_dezha,
            'a': a,
            'b':b,
            'username': username,
        #Информация для таблицы с расходом
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

    }
    return render(request, 'base.html', context)



def login_view(request):
    context = {}  # <-- Добавляем базовый контекст, чтобы избежать ошибки

    if request.method == 'POST':
        print("POST данные:", request.POST)
        form = LoginForm(request.POST)
        print("Ошибки валидации:", form.errors.as_json())

        if form.is_valid():
            user_id = int(form.cleaned_data['subcategory'])
            print(user_id)
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.get(id=user_id)
                user = authenticate(request,username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    redirect_params = {
                        'param1': user.username,
                        'param2': user.position,
                    }
                    return redirect('base', **redirect_params)
                else:
                    context['err'] = True  # <-- Гарантируем, что context существует
            except CustomUser.DoesNotExist:
                form.add_error('subcategory', "Пользователь не найден")
        else:
            form = LoginForm()
            err = True
            nach = list(CustomUser.objects.filter(username__icontains="Начальник").order_by("username").values_list("id", "username"))
            fak = list(CustomUser.objects.filter(username__icontains="факультету").order_by("username").values_list("id", "username"))
            kaf = list(CustomUser.objects.filter(username__icontains="кафедре").order_by("username").values_list("id", "username"))
            kurs = list(CustomUser.objects.filter(username__icontains="курс").order_by("username").values_list("id", "username"))

            context = {
                'form': form,
                'err': err,
                'nach': json.dumps(nach, ensure_ascii=False),
                'fak': json.dumps(fak, ensure_ascii=False),
                'kaf': json.dumps(kaf, ensure_ascii=False),
                'kurs': json.dumps(kurs, ensure_ascii=False),
            }
            return render(request, 'login.html', context)
    err = None
    form = LoginForm()
    nach = list(CustomUser.objects.filter(username__icontains="Начальник").order_by("username").values_list("id", "username"))
    fak = list(CustomUser.objects.filter(username__icontains="факультету").order_by("username").values_list("id", "username"))
    kaf = list(CustomUser.objects.filter(username__icontains="кафедре").order_by("username").values_list("id", "username"))
    kurs = list(CustomUser.objects.filter(username__icontains="курс").order_by("username").values_list("id", "username"))
    context = {
        'form': form,
        'err': err,
        'nach': json.dumps(nach, ensure_ascii=False),
        'fak': json.dumps(fak, ensure_ascii=False),
        'kaf': json.dumps(kaf, ensure_ascii=False),
        'kurs': json.dumps(kurs, ensure_ascii=False),
    }
    return render(request, 'login.html', context)



