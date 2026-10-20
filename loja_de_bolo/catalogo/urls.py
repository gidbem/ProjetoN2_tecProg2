from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('jogo/<int:pk>/', views.detalhes, name='detalhes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/novo/', views.jogo_criar, name='jogo_criar'),
    path('dashboard/<int:pk>/editar/', views.jogo_editar, name='jogo_editar'),
    path('dashboard/<int:pk>/excluir/', views.jogo_excluir, name='jogo_excluir'),
]