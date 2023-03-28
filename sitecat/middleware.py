from pprint import pprint
from graphql.execution.base import ResolveInfo
from .dataloaders import HomeLoader, HumanLoader, BreedLoader


class DataloaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.home_loader = HomeLoader()
        request.owner_loader = HumanLoader()
        request.breed_loader = BreedLoader()
        return self.get_response(request)
