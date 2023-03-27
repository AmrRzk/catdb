from promise.dataloader import DataLoader
from promise import Promise
from .models import Home
from asgiref.sync import sync_to_async
import asyncio

import logging

logger = logging.getLogger()


class HomeLoader(DataLoader):

    def get_home_map(self, homes):
        return {home.id: home for home in homes}

    def batch_load_fn(self, keys):
        homes = Home.objects.filter(id__in=keys)
        home_map = self.get_home_map(homes)
        return Promise.resolve([home_map.get(home_id) for home_id in keys])
