from django.contrib import admin
from .models import Container, WaterQuality, WaterQuantity

admin.site.register(Container)
admin.site.register(WaterQuantity)
admin.site.register(WaterQuality)
