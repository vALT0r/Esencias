from django.urls import path
from Apps.Esencias.views import *

urlpatterns = [
    path('esencias/', esencias, name='esencias'),
    path('esencias/<int:id>', esencias, name='esencias'),
    path('sintomas/', sintomas, name='sintomas'),
    path('subsintomas/<int:id>', subsintomas, name='subsintomas'),
    path('esenciadesc/<int:id>/<int:sintoma>/<int:formula>/<str:string>/<int:superformula>', esenciadesc, name='esenciadesc'),
    path('formulas/', formulas, name='formulas'),
    path('formula/<int:id>/<int:sintoma>/<str:string>/<int:superformula>', formula, name='formula'),
    path('search/', search, name='search'),
    path('fisicos/', fisicos, name='fisicos'),
    path('fisico/<int:id>', fisico, name='fisico'),
    # path('paciente/listar', listar, name='listar'),
    path('paciente/<int:id>', paciente, name='paciente'),
    path('paciente/add', add, name='add'),
    path('paciente/nuevaconsulta/<int:id>', nuevaconsulta, name='nuevaconsulta'),

]
