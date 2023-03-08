from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Human, Home, Cat, Breed


@registry.register_document
class HumanDocument(Document):
    class Index:
        name = "humans"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Human
        fields = ["id", "name", "description"]
