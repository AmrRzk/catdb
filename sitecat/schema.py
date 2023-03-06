import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django_extras import DjangoObjectField, DjangoFilterListField, DjangoSerializerType
from graphene_django.rest_framework.serializer_converter import convert_serializer_field

from rest_framework import serializers

from .filters import HumanFilter, CatFilter, HomeFilter, BreedFilter
from .models import Human, Cat, Home, Breed
from .serializer import HumanSerializer, CatSerializer, HomeSerializer, BreedSerializer


class HumanType(DjangoObjectType):
    class Meta:
        model = Human
        description = "Single User Type"
        filterset_class = HumanFilter


class CatType(DjangoObjectType):
    class Meta:
        model = Cat
        filterset_class = CatFilter


class HomeType(DjangoObjectType):
    class Meta:
        model = Home
        filterset_class = HomeFilter


class BreedType(DjangoObjectType):
    class Meta:
        model = Breed
        filterset_class = BreedFilter


class HumanModelType(DjangoSerializerType):

    class Meta:
        serializer_class = HumanSerializer
        # filterset_class = HumanFilter


class CatModelType(DjangoSerializerType):
    class Meta:
        serializer_class = CatSerializer
        filterset_class = CatFilter


class BreedModelType(DjangoSerializerType):
    class Meta:
        serializer_class = BreedSerializer
        filterset_class = BreedFilter


class HomeModelType(DjangoSerializerType):
    class Meta:
        serializer_class = HomeSerializer
        filterset_class = HomeFilter


class Query(graphene.ObjectType):

    all_humans = DjangoFilterListField(HumanType)
    all_cats = DjangoFilterListField(CatType)
    all_homes = DjangoFilterListField(HomeType)
    all_breeds = DjangoFilterListField(BreedType)

    human = DjangoObjectField(HumanType)
    cat = DjangoObjectField(CatType)
    home = DjangoObjectField(HomeType)
    breed = DjangoObjectField(BreedType)


class Mutation(graphene.ObjectType):
    create_human = HumanModelType.CreateField(description="Create Human")
    update_human = HumanModelType.UpdateField(description="Update Human")
    delete_human = HumanModelType.DeleteField(description="Delete Human")

    create_cat = CatModelType.CreateField(description="Create Cat")
    update_cat = CatModelType.UpdateField(description="Update Cat")
    delete_cat = CatModelType.DeleteField(description="Delete Cat")

    create_breed = BreedModelType.CreateField(description="Create Breed")
    update_breed = BreedModelType.UpdateField(description="Update Breed")
    delete_breed = BreedModelType.DeleteField(description="Delete Breed")

    create_home = HomeModelType.CreateField(description="Create Home")
    update_home = HomeModelType.UpdateField(description="Update Home")
    delete_home = HomeModelType.DeleteField(description="Delete Home")


schema = graphene.Schema(query=Query, mutation=Mutation)
