from .models import Cat, Human, Breed, Home, Gender
from rest_framework import serializers
from pprint import pprint


class HomeSerializer(serializers.ModelSerializer):
    house_type = serializers.CharField(max_length=2, required=False)
    address = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = Home
        fields = ["id", "name", "address", "house_type"]


class HumanSerializer(serializers.ModelSerializer):
    home = HomeSerializer(required=False)
    gender = serializers.ChoiceField(
        choices=Gender.choices, required=False)
    description = serializers.CharField(max_length=200, required=False)
    birth_date = serializers.DateField(required=False)

    class Meta:
        model = Human
        fields = ["id", "name", "gender", "birth_date", "description", "home"]

    # if no ID is provided, it will go to this create function
    def create(self, validated_data):
        print("Went into create")
        home_data = validated_data.pop('home')

        # Creates new home if home is created, otherwise get from existing data
        home, created = Home.objects.get_or_create(**home_data)
        human = Human.objects.create(home=home, **validated_data)
        return human

    # if ID is provided, it will lookup and get the related instance
    def update(self, instance, validated_data):
        print("Went into update")
        home_data = validated_data.pop('home')

        # Creates new home if home is created, otherwise get from existing data
        home, created = Home.objects.get_or_create(**home_data)

        instance.home = home
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class BreedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=70, required=False)
    description = serializers.CharField(max_length=700, required=False)
    origin = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Breed
        fields = ["id", "name", "origin", "description"]


class CatSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    owner = HumanSerializer()
    gender = serializers.ChoiceField(
        choices=Gender.choices, required=False)

    class Meta:
        model = Cat
        fields = "__all__"

    def create(self, validated_data):
        print("it entered create cat")
        pprint(validated_data)
        try:
            owner_data = validated_data.pop('owner')
            owner, _ = Human.objects.get_or_create(**owner_data)

            breed_data = validated_data.pop('breed')
            breed, _ = Breed.objects.get_or_create(**breed_data)

            cat = Cat.objects.create(
                owner=owner, breed=breed, **validated_data)
            return cat
        except Exception as e:
            pprint(e)
            return {'errors': [{'message': str(e)}]}

    def update(self, instance: Cat, validated_data):
        print("it entered update cat")

        try:
            owner_data = validated_data.pop('owner')
            owner, _ = Human.objects.get_or_create(**owner_data)

            breed_data = validated_data.pop('breed')
            breed, _ = Breed.objects.get_or_create(**breed_data)

            instance.owner = owner
            instance.breed = breed

            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            instance.save()
            return instance
        except Exception as e:
            return {'errors': [{'message': str(e)}]}
