from django.urls import path
from .views import Home, PokemonList, PokemonDetail, FeedingListCreate, FeedingDetail

urlpatterns = [
        path('', Home.as_view(), name='home'),
        path('pokemon/', PokemonList.as_view(), name='pokemon-list'),
        path('pokemon/<int:id>/', PokemonDetail.as_view(), name='pokemon-detail'),
        path('pokemon/<int:pokemon_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
        path('pokemon/<int:pokemon_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
]

