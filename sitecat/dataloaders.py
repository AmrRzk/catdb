from aiodataloader import DataLoader
from .models import Home
from asgiref.sync import sync_to_async
import asyncio


class HomeLoader(DataLoader):

    @sync_to_async
    def get_home_map(self, homes):
        return {home.id: home for home in homes}

    async def batch_load_fn(self, keys):
        print("Got into batch loader")
        homes = Home.objects.filter(id__in=keys)
        home_map = await self.get_home_map(homes)
        return [home_map.get(home_id) for home_id in keys]
