import graphene
from graphene_django import DjangoObjectType

from .models import Human, Cat, Home, Breed


class HumanType(DjangoObjectType):
    class Meta:
        model = Human
        fields = ["id", "name", "gender", "birth_date",
                  "description", "home", "cat_set"]


class CatType(DjangoObjectType):
    class Meta:
        model = Cat
        fields = ["id", "name", "gender", "birth_date",
                  "description", "breed", "owner"]


class HomeType(DjangoObjectType):
    class Meta:
        model = Home
        fields = ["id", "name", "address", "house_type", "human_set"]


class BreedType(DjangoObjectType):
    class Meta:
        model = Breed
        fields = ["id", "name", "origin", "description"]


class Query(graphene.ObjectType):
    all_humans = graphene.List(HumanType)
    all_cats = graphene.List(CatType)
    all_homes = graphene.List(HomeType)
    all_breeds = graphene.List(BreedType)

    human_by_name = graphene.Field(
        HumanType, name=graphene.String(required=True)
    )
    cat_by_name = graphene.Field(CatType, name=graphene.String(required=True))
    home_by_name = graphene.Field(
        HomeType, name=graphene.String(required=True)
    )
    breed_by_name = graphene.Field(
        BreedType, name=graphene.String(required=True))

    def resolve_all_humans(root, info):
        return Human.objects.all()

    def resolve_all_cats(root, info):
        return Cat.objects.all()

    def resolve_all_homes(root, info):
        return Home.objects.all()

    def resolve_all_breeds(root, info):
        return Breed.objects.all()

    def resolve_human_by_name(root, info, name):
        return Human.objects.get(name=name)

    def resolve_cat_by_name(root, info, name):
        return Cat.objects.get(name=name)

    def resolve_home_by_name(root, info, name):
        return Home.objects.get(name=name)

    def resolve_breed_by_name(root, info, name):
        return Breed.objects.get(name=name)


schema = graphene.Schema(query=Query)
