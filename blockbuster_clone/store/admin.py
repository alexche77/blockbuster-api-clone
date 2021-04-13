from django.contrib import admin
from blockbuster_clone.store.models import (
    RentRequest,
    RentReturn,
    Sale,
    Purchase,
    InventoryAdjustment,
    DefectiveReturn,
)

# Register your models here.
admin.site.register(RentRequest)
admin.site.register(RentReturn)
admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(InventoryAdjustment)
admin.site.register(DefectiveReturn)