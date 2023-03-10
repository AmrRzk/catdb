from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Human, Home, Cat, Breed


@registry.register_document
class HumanDocument(Document):

    home = fields.ObjectField(
        properties={
            "name": fields.TextField()
        }
    )

    class Index:
        name = "humans"

    class Django:
        model = Human
        fields = ["id", "name", "description", "gender", "birth_date"]


@registry.register_document
class HomeDocument(Document):
    class Index:
        name = "homes"

    class Django:
        model = Home
        fields = ["id", "name", "house_type", "address"]


@registry.register_document
class CatDocument(Document):

    owner = fields.ObjectField(
        properties={
            "name": fields.TextField()
        }
    )

    breed = fields.ObjectField(
        properties={
            "name": fields.TextField()
        }
    )

    class Index:
        name = "cats"

    class Django:
        model = Cat
        fields = ["id", "name", "description", "gender", "birth_date"]


@registry.register_document
class BreedDocument(Document):
    class Index:
        name = "breeds"

    class Django:
        model = Breed
        fields = ["id", "name", "origin", "description"]
