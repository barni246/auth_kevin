from django.contrib import admin
from .models import Manufacturer, ManufacturerUser, Product

admin.site.register(Manufacturer)
admin.site.register(ManufacturerUser)
admin.site.register(Product)
