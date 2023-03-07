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
        name = "human"

    class Django:
        model = Human
        fields = ["id", "name", "description", "gender"]
