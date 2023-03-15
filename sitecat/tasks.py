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

        breeds.append(breed)

    # get the breeds from db and compare it with the breeds from the API so that we don't add duplicates
    db_breeds = [breed.name for breed in Breed.objects.all()]

    new_breeds = [
        Breed(**new_breed) for new_breed in breeds if new_breed['name'] not in db_breeds]

    Breed.objects.bulk_create(new_breeds)

    return "Data successfully updated"
