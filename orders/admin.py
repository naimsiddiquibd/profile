from django.contrib import admin
from orders.models import basicpack
from orders.models import standardpack
from orders.models import propack
# Register your models here.

admin.site.register(basicpack)
admin.site.register(standardpack)
admin.site.register(propack)
