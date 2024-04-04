from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pokemon, Feeding, Toy
from .serializers import PokemonSerializer, FeedingSerializer, ToySerializer, UserSerializer
from rest_framework import generics, filters, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied

class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the pokemon-collector api home route!'}
    return Response(content)

class PokemonList(generics.ListCreateAPIView):
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type1', 'type2', 'user']
    ordering_fields = ['name', 'type1', 'type2', 'user']

    def get_queryset(self):
        user = self.request.user
        return Pokemon.objects.filter(user=user)

    def perfrom_create(self, serializer):
        serializer.save(user=self.request.user)

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PokemonSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Pokemon.objects.filter(user=user)

    def retrieve(self, request, *args, **kwards):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        toys_not_associated = Toy.objects.exclude(id__in=instance.toys.all())
        toys_serializer = ToySerializer(toys_not_associated, many=True)

        return Response({
            'pokemon': serializer.data,
            'toys_not_associated': toys_serializer.data
            })

    def perform_update(self, serializer):
        pokemon = self.get_object()
        if pokemon.user != self.request.user:
            raise PermissionDenied({'message': "You do not have permission to edit this cat."})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied({'message': "You do not have permission to delete this cat."})
        instance.delete()

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

class ToyList(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    lookup_field = 'id'

#class ToyListCreate(generics.ListCreateAPIView):
#    serializer_class = ToySerializer

#    def get_queryset(self)
#        pokemon_id = self.kwargs['pokemon_id']
#        return Toy.objects.filter(pokemon_id = pokemon_id)

#    def perform_create(self, serializer):
#        pokemon_id = self.kwargs['pokemon_id']
#        pokemon = Pokemon.objects.get(id=pokemon_id)
#        serializer.save(pokemon=pokemon)

class AddToyToPokemon(APIView):
    def post(self, request, pokemon_id, toy_id):
        pokemon = Pokemon.objects.get(id=pokemon_id)
        toy = Toy.objects.get(id=toy_id)
        pokemon.toys.add(toy)
        return Response({'message': f'Toy {toy.name} added to Pokemon {pokemon.name}'})

class RemoveToyToPokemon(APIView):
    def post(self, request, pokemon_id, toy_id):
        pokemon = Pokemon.objects.get(id=pokemon_id)
        toy = Toy.objects.get(id=toy_id)
        pokemon.toys.remove(toy)
        return Response({'message': f'Toy {toy.name} removed from Pokemon {pokemon.name}'})

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })
