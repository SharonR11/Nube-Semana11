from django.urls import path
from . import views

urlpatterns = [

    path('', views.menu, name='menu'),
    path('registrar/',views.insertarpersona,name='registrar'),
    path('eliminar/<idPersona>/', views.eliminar, name='eliminar'),
    path('data/<int:idPersona>',views.datapersona, name='data'),
    path('modificar/<int:idPersona>/', views.editar, name='editar'),
]