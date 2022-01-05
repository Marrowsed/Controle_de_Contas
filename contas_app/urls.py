from django.urls import path
from . import views

urlpatterns = [

    ##MODAL VIEW##
    path('', views.index, name="index"),
    path('banco/<str:pk>', views.banco, name='banco'),
    path('banco/poupanca/<str:pk>', views.poupanca, name='poupanca'),
    path('credito/<str:pk>', views.credito, name='credito'),
    path('corrente/<str:pk>', views.corrente, name='corrente'),

    ##MODAL DE INTERAÇÃO
    #------POUPANÇA-----
    path('banco/poupanca/<str:pk>/aplicar', views.aplicar, name='aplicar'),
    path('banco/poupanca/<str:pk>/resgatar', views.resgatar, name='resgatar'),
    path('banco/poupanca/<str:pk>/transferir', views.transferir, name='transferir'),
    #------CONTA CRÉDITO-----
    path('credito/<str:pk>/comprar', views.credito, name='comprar'),
    path('credito/<str:pk>/pagar', views.credito, name='pagar'),
    #------CONTA CORRENTE-----
    path('corrente/<str:pk>/depositar', views.corrente, name='depositar'),
    path('corrente/<str:pk>/retirar', views.corrente, name='retirar'),
]