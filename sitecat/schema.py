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


class HumanSchema:
    class Mutation(graphene.Mutation):
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

            return HumanSchema.Mutation(human=human)

    class Delete(graphene.Mutation):
        class Arguments:
            id = graphene.ID()
        human = graphene.Field(Human)

        @classmethod
        def mutate(cls, root, info, id):
            human = Human.objects.get(id=id)
            human.delete()
            return HumanSchema.Delete(human=human)


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


class BreedMutation():

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        origin = graphene.String(required=True)
        description = graphene.String(required=True)

    breed = graphene.Field(BreedType)

    @classmethod
    def mutate(cls, root, info, id, name, origin, description):
        breed = Breed.objects.get(id=id)
        breed.name = name
        breed.origin = origin
        breed.description = description
        breed.save()

        return BreedMutation(breed=breed)


class CatMutation():
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
        gender = graphene.String(required=True)
        birth_date = graphene.Date(required=True)
        description = graphene.String()
        breed_name = graphene.String()
        owner_name = graphene.String()

    cat = graphene.Field(CatType)

    @classmethod
    def mutate(cls, root, info, id, name, gender, birth_date, description, breed_name, owner_name):
        cat = Cat.objects.get(id=id)
        cat.name = name
        cat.gender = gender
        cat.birth_date = birth_date
        cat.description = description
        cat.breed = Breed.objects.get(name=breed_name)
        cat.owner = Human.objects.get(name=owner_name)
        cat.save()

        return CatMutation(cat=cat)


class Mutation(graphene.ObjectType):
    update_human = HumanMutation.Field()
    update_home = HomeMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
