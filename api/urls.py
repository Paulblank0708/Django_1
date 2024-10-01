from django.urls import include, path
from . import  views


urlpatterns = [
    path('/', views.raiz),
    path('sobre/', views.sobreNos),
    path('contatos/', views.meusContatos),

]
