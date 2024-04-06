from django.contrib import admin
from .models import Person, Company, Address, CarpoolGroup


admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(CarpoolGroup)
