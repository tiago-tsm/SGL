from django.contrib import admin
from . import models


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'enterprise', 'telephone',)
    search_fields = ('name',)


admin.site.register(models.CustomerRegistration, RegistrationAdmin)

