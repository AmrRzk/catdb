import graphene
from graphene import Enum
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django_extras import DjangoListObjectType, DjangoListObjectField, DjangoObjectField, DjangoFilterListField

from django.core.cache import cache
from pprint import pprint

from .filters import HumanFilter, CatFilter, HomeFilter, BreedFilter
from .models import Human, Cat, Home, Breed, Gender
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


class Query(graphene.ObjectType):

    all_humans = DjangoFilterListField(HumanType)
    all_cats = DjangoFilterListField(CatType)
    all_homes = DjangoFilterListField(HomeType)
    all_breeds = DjangoFilterListField(BreedType)

    human = DjangoObjectField(HumanType)
    cat = DjangoObjectField(CatType)
    home = DjangoObjectField(HomeType)
    breed = DjangoObjectField(BreedType)

    latest_cat = graphene.String()

    def resolve_latest_cat(root, info):

        latest_name = cache.get('name')

        if latest_name is None:
            latest_cat = Cat.objects.order_by('id')[0]
            latest_name = latest_cat.name
            cache.set('name', latest_name, 1500)

        return latest_name


class HumanMutation(SerializerMutation):
    class Meta:
        serializer_class = HumanSerializer


class DeleteHuman(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        human = Human.objects.get(pk=kwargs.get('id'))
        human.delete()
        return DeleteHuman(ok=True)


class HomeMutation(SerializerMutation):
    class Meta:
        serializer_class = HomeSerializer
        model_operations = ['create', 'update']
        lookup_field = "id"


class DeleteHome(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        home = Home.objects.get(pk=kwargs.get('id'))
        Home.delete()
        return DeleteHome(ok=True)


class BreedMutation(SerializerMutation):
    class Meta:
        serializer_class = BreedSerializer
        model_operations = ['create', 'update']
        lookup_field = "id"


class DeleteBreed(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        breed = Breed.objects.get(pk=kwargs.get('id'))
        breed.delete()
        return DeleteBreed(ok=True)


class CatMutation(SerializerMutation):

    class Meta:
        serializer_class = CatSerializer
        model_operations = ['create', 'update']
        lookup_field = "id"

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        context = super().get_serializer_kwargs(root, info, **input)

        context['data']['gender'] = context['data']['gender'].name
        breed_data = context['data']['breed']
        breed = Breed.objects.get(**breed_data)
        if breed is not None:
            context['data']['breed']['id'] = breed.pk
        return context


class DeleteCat(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        cat = Cat.objects.get(pk=kwargs.get('id'))
        cat.delete()
        return DeleteCat(ok=True)


class Mutation(graphene.ObjectType):

    # Update or Create
    create_or_update_human = HumanMutation.Field()
    create_or_update_home = HomeMutation.Field()
    create_or_update_cat = CatMutation.Field()
    create_or_update_breed = BreedMutation.Field()

    # Delete
    delete_human = DeleteHuman.Field()
    delete_home = DeleteHome.Field()
    delete_cat = DeleteCat.Field()
    delete_breed = DeleteBreed.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
