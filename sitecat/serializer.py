from .models import Cat, Human, Breed, Home
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    house_type = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = Home
        fields = ["id", "name", "address", "house_type"]


class HumanSerializer(serializers.ModelSerializer):
    home = HomeSerializer()
    gender = serializers.CharField(max_length=1, required=False)
    description = serializers.CharField(max_length=200, required=False)
    birth_date = serializers.DateField(required=False)

    class Meta:
        model = Human
        fields = "__all__"
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }

    # if no ID is provided, it will go to this create function
    def create(self, validated_data):
        home_data = validated_data.pop('home')

        # Creates new home if home is created, otherwise get from existing data
        home, created = Home.objects.get_or_create(**home_data)
        human = Human.objects.create(home=home, **validated_data)
        return human

    # if ID is provided, it will lookup and get the related instance
    def update(self, instance, validated_data):
        home_data = validated_data.pop('home')

        # Creates new home if home is created, otherwise get from existing data
        home, created = Home.objects.get_or_create(**home_data)

        instance.home = home
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class BreedSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = Breed
        fields = ["id", "name", "origin", "description"]


class CatSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    owner = HumanSerializer()
    gender = serializers.CharField(max_length=1)

    class Meta:
        model = Cat
        fields = "__all__"

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        owner, _ = Human.objects.get_or_create(**owner_data)

        breed_data = validated_data.pop('breed')
        breed, _ = Breed.objects.get_or_create(**breed_data)

        cat = Cat.objects.create(owner=owner, breed=breed, **validated_data)
        return cat

    def update(self, instance: Cat, validated_data):

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
