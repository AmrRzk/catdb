import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation

from .models import Human, Cat, Home, Breed
from .serializer import HumanSerializer, CatSerializer, HomeSerializer, BreedSerializer


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
        fields = ["id", "name", "address", "house_type"]


class BreedType(DjangoObjectType):
    class Meta:
        model = Breed
        fields = ["id", "name", "origin", "description"]


class Query(graphene.ObjectType):

    all_humans = graphene.List(HumanType)
    all_cats = graphene.List(CatType)
    all_homes = graphene.List(HomeType)
    all_breeds = graphene.List(BreedType)

    human_by_id = graphene.Field(
        HumanType, id=graphene.ID(required=True)
    )
    cat_by_id = graphene.Field(CatType, id=graphene.ID(required=True))
    home_by_id = graphene.Field(
        HomeType, id=graphene.ID(required=True)
    )
    breed_by_id = graphene.Field(
        BreedType, id=graphene.ID(required=True)
    )

    def resolve_all_humans(root, info):
        return Human.objects.all()

    def resolve_all_cats(root, info):
        return Cat.objects.all()

    def resolve_all_homes(root, info):
        return Home.objects.all()

    def resolve_all_breeds(root, info):
        return Breed.objects.all()

    def resolve_human_by_id(root, info, id):
        return Human.objects.get(id=id)

    def resolve_cat_by_id(root, info, id):
        return Cat.objects.get(id=id)

    def resolve_home_by_id(root, info, id):
        return Home.objects.get(id=id)

    def resolve_breed_by_id(root, info, id):
        return Breed.objects.get(id=id)


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
