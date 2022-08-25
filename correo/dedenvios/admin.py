from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(neighborhood)
admin.site.register(Zone)
admin.site.register(originPerson)
admin.site.register(destinyPerson)
admin.site.register(Package)
admin.site.register(logperson)