from django.contrib import admin

# Register your models here.
# Register your models here.
from experience.models import experience
from experience.models import education
from experience.models import workhis

admin.site.register(experience)
admin.site.register(education)
admin.site.register(workhis)
