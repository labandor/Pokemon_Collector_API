from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pokemon
from .serializers import PokemonSerializer
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
