from celery import shared_task
import requests
from sitecat.models import Breed


@shared_task(bind=True)
def update_breed(self):
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    data = response.json()

    breeds = []

    for breed_data in data:
        breed = {
            "name": breed_data["name"],
            "description": breed_data["description"],
            "origin": breed_data["origin"]
        }

        breeds.append(Breed(**breed))

    Breed.objects.bulk_create(
        breeds, ignore_conflicts=True, unique_fields=['name'])

    return "Data successfully updated"
