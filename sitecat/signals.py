from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from .models import Cat


@receiver(post_save, sender=Cat)
def add_cat(sender, instance, **kwargs):
    cache.set('name', instance.name, 1500)
