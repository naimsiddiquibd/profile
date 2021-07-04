from django.contrib import admin
from about.models import about
from about.models import skills
from about.models import counter
# Register your models here.

admin.site.register(about)
admin.site.register(skills)
admin.site.register(counter)
