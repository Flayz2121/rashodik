from django.contrib import admin
from django.urls import path, include
from authin.views import base_view,login_view
from main.views import edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('base/<str:param1>&&<str:param2>', base_view, name='base'),
    path('base/edit/<str:param1>/', edit, name='edit'),
]
