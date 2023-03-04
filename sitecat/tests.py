from django.test import TestCase

from .models import Human, Cat, Breed, Home
from .schema import schema

# Create your tests here.


class APITestCase(TestCase):
    def setUp(self):
        home_1_dict = {
            "name": "Cozy Home",
            "house_type": "TERRACE",
            "address": "12, Jalan 5, Block 8"
        }
        home_1 = Home.objects.create(**home_1_dict)

        human_1_dict = {
            "name": "Bryan",
            "description": "A very big person",
            "gender": "M",
            "birth_date": "2000-10-20",
            "home": home_1
        }

        human_1 = Human.objects.create(**human_1_dict)

        human_2_dict = {
            "name": "Mark Study",
            "description": "A very studious person",
            "gender": "M",
            "birth_date": "2002-12-12",
            "home": home_1
        }

        human_2 = Human.objects.create(**human_2_dict)

        breed_1_dict = {
            "name": "Schrodingers",
            "origin": "German",
            "description": "Oh no...."
        }

        breed_1 = Breed.objects.create(**breed_1_dict)

        cat_1_dict = {
            "name": "Fluff",
            "gender": "F",
            "birth_date": "2020-02-20",
            "description": "Very fluffy cat",
            "owner": human_1,
            "breed": breed_1
        }

        cat_1 = Cat.objects.create(**cat_1_dict)

    def test_allhumans(self):
        query = """
        query {
            allHumans {
                name
                home {
                    name
                }
            }
        }
        """
        result = schema.execute(query)
        assert_query = [{
            "name": "Bryan",
            "home": {
                "name": "Cozy Home"
            }
        }, {
            "name": "Mark Study",
            "home": {
                "name": "Cozy Home"
            }
        }]

        self.assertEqual(result.data["allHumans"], assert_query)

    def test_allhumans_filter(self):
        query = """
        query {
            allHumans(name_Icontains:"Mark") {
                name
                home {
                    name
                }
            }
        }
        """
        result = schema.execute(query)
        assert_query = [{
            "name": "Mark Study",
            "home": {
                "name": "Cozy Home"
            }
        }]
        self.assertEqual(result.data["allHumans"], assert_query)
