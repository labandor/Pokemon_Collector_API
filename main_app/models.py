from django.db import models
from django.contrib.auth.models import User

# Create your models here.

POKEMON_TYPES = [
        ('Norm', 'Normal'),
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Electric', 'Electric'),
        ('Grass', 'Grass'),
        ('Ice', 'Ice'),
        ('Fighting', 'Fighting'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Flying', 'Flying'),
        ('Psychic', 'Psychic'),
        ('Bug', 'Bug'),
        ('Rock', 'Rock'),
        ('Ghost', 'Ghost'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
        ('Stellar', 'Stellar'),
        ('N/A', 'N/A'),
]

POKEMON_FOOD = [
        ('Berries', 'Berries'),
        ('PokeBlock','Pokeblock'),
        ('Poffin', 'Poffin'),
        ('Honey', 'Honey'),
        ('Aprijuice', 'Aprijuice'),
        ('PokePuffs', 'Poke Puffs'),
        ('PokeBeans', 'Poke Beans'),
        ('Curry', 'Curry'),
        ('Sandwich', 'Sandwiches'),
        ('Local', 'Local Specialty'),
]

class Toy(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name}'

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField()
    email = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()

    def __str__(self):
        return self.username

class Pokemon(models.Model):
    name = models.CharField(max_length=13)
    species = models.CharField(max_length=13)
    type1 = models.CharField(choices=POKEMON_TYPES)
    type2 = models.CharField(choices=POKEMON_TYPES)
    sex = models.CharField(max_length=6, choices = [('Male', 'Male'), ('Female', 'Female')])
    size_cm = models.IntegerField()
    weight_lbs = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.name} - {self.species} - {self.type1}, {self.type2}'

class Photo(models.Model):
    url = models.CharField()
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE, related_name='phtos')

    def __str__(self):
        return self.url

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(choices=POKEMON_FOOD)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='feeding')

    def __str__(self):
        return f'{self.meal} --- {self.pokemon.name}'

    class Meta:
        ordering = ['-date']


