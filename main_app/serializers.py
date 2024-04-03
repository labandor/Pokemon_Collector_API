from rest_framework import serializers
from .models import Pokemon, User, Toy, Feeding, Photo
from rest_framework.validators import UniqueTogetherValidator

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        Validators = [
                UniqueTogetherValidator(
                    queryset = Pokemon.objects.all(),
                    fields = ['name', 'species', 'user'],
                    message = 'oh no this is a double'
                    )
                ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('pokemon',)

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
