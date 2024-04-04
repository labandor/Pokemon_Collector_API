from rest_framework import serializers
from .models import Pokemon, User, Toy, Feeding, Photo
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):
    toys = ToySerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

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
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
                )

        return user


class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('pokemon',)

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
