from pprint import pprint
from graphql.execution.base import ResolveInfo
from .dataloaders import HomeLoader


class DataLoaderMiddleware(object):
    def resolve(self, next, root, info: ResolveInfo, **args):
        if info.field_name == "allHumans":
            info.context.loader = HomeLoader()
        return next(root, info, **args)
