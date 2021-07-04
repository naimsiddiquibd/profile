from django.contrib import admin

# Register your models here.
from Content.models import Settings
from Content.models import Logo
from Content.models import Menu

admin.site.register(Settings)
admin.site.register(Logo)
admin.site.register(Menu)
