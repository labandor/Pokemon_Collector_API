from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pokemon, Feeding
from .serializers import PokemonSerializer, FeedingSerializer
from rest_framework import generics, filters

class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the pokemon-collector api home route!'}
    return Response(content)

class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type1', 'type2', 'user']
    ordering_fields = ['name', 'type1', 'type2', 'user']

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    lookup_field = 'id'

class FeedingListCreate(generics.ListCreateAPIView):
  serializer_class = FeedingSerializer

  def get_queryset(self):
    pokemon_id = self.kwargs['pokemon_id']
    return Feeding.objects.filter(pokemon_id=pokemon_id)

  def perform_create(self, serializer):
    pokemon_id = self.kwargs['pokemon_id']
    pokemon = Pokemon.objects.get(id=pokemon_id)
    serializer.save(pokemon=pokemon)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeedingSerializer
  lookup_field = 'id'

  def get_queryset(self):
    pokemon_id = self.kwargs['pokemon_id']
    return Feeding.objects.filter(pokemon_id=pokemon_id)

