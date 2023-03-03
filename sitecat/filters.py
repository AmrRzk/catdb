import django_filters
from .models import Human, Home, Cat, Breed


class HumanFilter(django_filters.FilterSet):
    id = django_filters.rest_framework.NumberFilter(
        field_name="id", required=False)

    class Meta:
        model = Human
        fields = {
            "name": ("iexact", "icontains"),
            "gender": ("exact",),
            "description": ("icontains",),
            "birth_date": ("gte", "lte")
        }


class HomeFilter(django_filters.FilterSet):
    id = django_filters.rest_framework.NumberFilter(
        field_name="id", required=False)

    class Meta:
        model = Home
        fields = {
            "name": ("iexact", "icontains"),
            "address": ("iexact", "icontains"),
            "house_type": ("exact", )
        }


class CatFilter(django_filters.FilterSet):
    id = django_filters.rest_framework.NumberFilter(
        field_name="id", required=False)

    class Meta:
        model = Cat
        fields = {
            "name": ("iexact", "icontains"),
            "gender": ("exact",),
            "description": ("icontains",),
            "birth_date": ("gte", "lte")
        }


class BreedFilter(django_filters.FilterSet):
    id = django_filters.rest_framework.NumberFilter(
        field_name="id", required=False)

    class Meta:
        model = Breed
        fields = {
            "name": ("iexact", "icontains"),
            "origin": ("iexact", "icontains"),
            "description": ("icontains",),

        }
