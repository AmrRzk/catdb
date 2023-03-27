from pprint import pprint
from graphql.execution.base import ResolveInfo
from .dataloaders import HomeLoader, HumanLoader, BreedLoader


class DataLoaderMiddleware(object):
    def resolve(self, next, root, info: ResolveInfo, **args):
        if info.field_name == "allHumans":
            info.context.loader = HomeLoader()
        elif info.field_name == "allCats":
            info.context.owner_loader = HumanLoader()
            info.context.breed_loader = BreedLoader()
        return next(root, info, **args)
