from django.contrib import admin
from . models import Device, Owner, Data

admin.site.register(Device)
admin.site.register(Owner)
admin.site.register(Data)

# Register your models here.
