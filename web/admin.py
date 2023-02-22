from django.contrib import admin

from .models import Human, Cat, Breed, Home
# Register your models here.
admin.site.register(Human)
admin.site.register(Cat)
admin.site.register(Breed)
admin.site.register(Home)
