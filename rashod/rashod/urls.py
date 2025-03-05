from django.contrib import admin
from django.urls import path, include
from authin.views import base_view,login_view
from main.views import edit_naryad, edit_uvolnenie, edit_bolen, edit_otpusk, fakultet, fakultet_all, make_kursants


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('base/<str:param1>&&<str:param2>', base_view, name='base'),
    path('base/edit_naryad/<str:param1>&&<int:param3>/', edit_naryad, name='edit_naryad'),
    path('base/edit_uvolnenie/<str:param1>&&<int:param3>/', edit_uvolnenie, name='edit_uvolnenie'),
    path('base/edit_bolen/<str:param1>&&<int:param3>/', edit_bolen, name='edit_bolen'),
    path('base/edit_otpusk/<str:param1>&&<int:param3>/', edit_otpusk, name='edit_otpusk'),
    path('base/make_kursants/<str:param1>&&<int:param3>/', make_kursants, name='make_kursants'),
    path('base/fakultet_all/<str:param1>&&<int:param2>/', fakultet_all, name='fakultet_all'),
    path('base/fakultet/<str:param1>&&<int:param2>/', fakultet, name='fakultet'),

]
