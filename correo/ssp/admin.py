from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Service)
admin.site.register(Zone)
admin.site.register(neighborhood)
admin.site.register(Person)
admin.site.register(Courier)
admin.site.register(PackageSending)