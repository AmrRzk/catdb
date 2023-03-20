from aiodataloader import DataLoader
from .models import Home


class HomeLoader(DataLoader):

    async def batch_load_fn(self, keys):
        await print("It got into batch loader")
        homes = await Home.objects.filter(id__in=keys).all()
        home_map = {home.id: home for home in homes}
        return [home_map.get(home_id) for home_id in keys]
