from aiodataloader import DataLoader
from .models import Home


class HomeLoader(DataLoader):

    async def batch_load_fn(self, keys):
        homes = await Home.objects.filter(id__in=keys)
        home_map = {home.id: home for home in homes}
        return await [home_map.get(home_id) for home_id in keys]
