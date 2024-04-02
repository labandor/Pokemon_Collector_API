from django.urls import path
from .views import Home, PokemonList, PokemonDetail

urlpatterns = [
        path('', Home.as_view(), name='home'),
        path('pokemon/', PokemonList.as_view(), name='pokemon-list'),
        path('pokemon/<int:id>/', PokemonDetail.as_view(), name='pokemon-detail'),
]

