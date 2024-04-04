from django.urls import path
from .views import Home, PokemonList, PokemonDetail, FeedingListCreate, FeedingDetail, ToyDetail, ToyList, AddToyToPokemon, RemoveToyToPokemon, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
        path('', Home.as_view(), name='home'),
        path('pokemon/', PokemonList.as_view(), name='pokemon-list'),
        path('pokemon/<int:id>/', PokemonDetail.as_view(), name='pokemon-detail'),
        path('pokemon/<int:pokemon_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
        path('pokemon/<int:pokemon_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
      #  path('pokemon/<int:pokemon_id>/toys/', ToyListCreate.as_view(), name='toy-list-create'),
        path('pokemon/toys/<int:id>/', ToyDetail.as_view(), name='toy-detail'),
        path('pokemon/toys/', ToyList.as_view(), name='toy-list'),
        path('pokemon/<int:pokemon_id>/add_toy/<int:toy_id>/', AddToyToPokemon.as_view(), name='add-toy-to-pokemon'),
        path('pokemon/<int:pokemon_id>/remove_toy/<int:toy_id>/', RemoveToyToPokemon.as_view(), name='remove-toy-to-pokemon'),
        path('users/register/', CreateUserView.as_view(), name='register'),
        path('users/login/', LoginView.as_view(), name='login'),
        path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
]

