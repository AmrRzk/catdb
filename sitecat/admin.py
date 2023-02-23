from django.contrib import admin

# Register your models here.

from .models import Human, Cat, Breed, Home
admin.site.register(Human)
admin.site.register(Cat)
admin.site.register(Breed)
admin.site.register(Home)
