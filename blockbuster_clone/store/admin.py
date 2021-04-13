from django.contrib import admin

from blockbuster_clone.store.models import Movement, PurchaseOrder

# Register your models here.
admin.site.register(Movement)
admin.site.register(PurchaseOrder)
