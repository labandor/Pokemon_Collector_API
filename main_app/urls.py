from django.urls import path
from .views import Home, PokemonList, PokemonDetail, FeedingListCreate, FeedingDetail, ToyListCreate, ToyDetail, ToyList

urlpatterns = [
        path('', Home.as_view(), name='home'),
        path('pokemon/', PokemonList.as_view(), name='pokemon-list'),
        path('pokemon/<int:id>/', PokemonDetail.as_view(), name='pokemon-detail'),
        path('pokemon/<int:pokemon_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
        path('pokemon/<int:pokemon_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
        path('pokemon/<int:pokemon_id>/toys', ToyListCreate.as_view(), name='toy-list-create'),
        path('pokemon/toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),
        path('pokemon/toys', ToyList.as_view(), name='toy-list'),
]

