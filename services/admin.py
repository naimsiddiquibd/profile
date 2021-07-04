from django.contrib import admin

# Register your models here.
from services.models import services
from services.models import items

admin.site.register(services)
admin.site.register(items)
