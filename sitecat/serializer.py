from .models import Cat, Human, Breed, Home
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ["id", "name", "address", "house_type"]


class HumanSerializer(serializers.ModelSerializer):
    home = HomeSerializer()

    class Meta:
        model = Human
        fields = "__all__"
        extra_kwargs = {
            'id': {'read_only': False, 'required': False}
        }

    def create(self, validated_data):
        print("It went into create")
        home_data = validated_data.pop('home')
        home, created = Home.objects.get_or_create(**home_data)
        human = Human.objects.create(home=home, **validated_data)
        return human

    def update(self, instance, validated_data):
        home_data = validated_data.pop('home')
        home, created = Home.objects.get_or_create(**home_data)

        instance.home = home
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "gender", "birth_date",
                  "description", "breed", "owner"]


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ["id", "name", "origin", "description"]
