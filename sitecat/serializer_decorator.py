from graphene_django.rest_framework.serializer_converter import get_graphene_type_from_serializer_field
from rest_framework import serializers
import graphene

print("It entered serializer_decorator.py")


@get_graphene_type_from_serializer_field.register(serializers.ChoiceField)
def convert_choices_to_string(field):
    return graphene.String


@get_graphene_type_from_serializer_field.register(serializers.CharField)
def convert_all_char_to_string(field):
    return graphene.String
