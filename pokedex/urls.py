from django.urls import path
from . import views


app_name = 'pokedex'

urlpatterns = [

    path('Pokemon/', views.poke_deck, name='poke_deck'),
    path('Pokemon/<int:id>/Info/', views.poke_info, name='poke_info'),

] 