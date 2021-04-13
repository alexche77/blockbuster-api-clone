from django.db.models.signals import pre_save
from django.dispatch import receiver

from blockbuster_clone.store.models import Movement


@receiver(pre_save, sender=Movement)
def set_unit_price(sender, instance, **kwargs):
    if instance.movement_type == Movement.MovementType.PURCHASE:
        instance.unit_price = instance.price / instance.quantity
