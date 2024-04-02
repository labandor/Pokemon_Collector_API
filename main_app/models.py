from django.db import models

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
        ('Ber', 'Berries'),
        ('PokeB','Pokeblock'),
        ('Pof', 'Poffin'),
        ('Hon', 'Honey'),
        ('Apri', 'Aprijuice'),
        ('PokeP', 'Poke Puffs'),
        ('PokeBe', 'Poke Beans'),
        ('Cur', 'Curry'),
        ('Sand', 'Sandwiches'),
        ('Local', 'Local Specialty'),
]

class Toy(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField()

    def __str__(self):
        return self.username

class Pokemon(models.Model):
    name = models.CharField(max_length=13)
    species = models.CharField(max_length=13, default='N/A')
    type1 = models.CharField(choices=POKEMON_TYPES)
    type2 = models.CharField(choices=POKEMON_TYPES)
    sex = models.CharField(max_length=6, choices = [('Boy', 'Male'), ('Girl', 'Female')])
    size_cm = models.IntegerField()
    weight_lbs = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemon')
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.name} - {self.type1} {self.type2}'

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
        return self.meal


