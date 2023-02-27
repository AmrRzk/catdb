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


class HumanMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        gender = graphene.String(required=True)
        birth_date = graphene.Date(required=True)
        description = graphene.String()
        home_name = graphene.String(required=True)

    human = graphene.Field(HumanType)

    @classmethod
    def mutate(cls, root, info, id,  name, gender, birth_date, description, home_name):
        human = Human.objects.get(id=id)
        human.name = name
        human.gender = gender
        human.birth_date = birth_date
        human.description = description
        human.home = Home.objects.get(name=home_name)
        human.save()
        print(human)

        return HumanMutation(human=human)


class HumanMutateName(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    human = graphene.Field(HumanType)

    @classmethod
    def mutate(cls, root, info, name, id):
        human = Human.objects.get(id=id)
        human.name = name
        human.save()

        return HumanMutateName(human=human)


class HomeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        house_type = graphene.String(required=True)

    home = graphene.Field(HomeType)

    @classmethod
    def mutate(cls, root, info, id, name, address, house_type):
        home = Home.objects.get(id=id)
        home.name = name
        home.address = address
        home.house_type = house_type
        home.save()

        return HomeMutation(home=home)


class Mutation(graphene.ObjectType):
    update_human = HumanMutation.Field()
    update_home = HomeMutation.Field()
    update_human_name = HumanMutateName.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
