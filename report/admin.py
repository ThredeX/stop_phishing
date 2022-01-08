from django.contrib import admin
from . import models
# Register your models here.


class PhishingAdmin(admin.ModelAdmin):
    list_display = ('domain', 'is_verified',)
    list_editable = ('is_verified',)


admin.site.register(models.PhishingUrl, PhishingAdmin)
