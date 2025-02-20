from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', view.saludo, name='saludo'),
    path('despedida/', view.despedida, name='despedida'),
    path('adulto/<int:edad>/', view.adulto, name='edad')
]
