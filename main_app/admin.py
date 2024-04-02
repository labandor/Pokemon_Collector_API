from django.contrib import admin
from .models import User, Pokemon, Photo, Feeding, Toy

# Register your models here.
admin.site.register(User)
admin.site.register(Pokemon)
admin.site.register(Photo)
admin.site.register(Feeding)
admin.site.register(Toy)
