from promise.dataloader import DataLoader
from promise import Promise
from .models import Home, Breed, Human


class HomeLoader(DataLoader):
    def batch_load_fn(self, keys):
        homes = Home.objects.in_bulk(keys)
        return Promise.resolve([homes.get(home_id) for home_id in keys])


class HumanLoader(DataLoader):
    def batch_load_fn(self, keys):
        humans = Human.objects.in_bulk(keys)
        return Promise.resolve([humans.get(human_id) for human_id in keys])


class BreedLoader(DataLoader):
    def batch_load_fn(self, keys):
        breeds = Breed.objects.in_bulk(keys)
        return Promise.resolve([breeds.get(breed_id) for breed_id in keys])
