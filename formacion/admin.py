from django.contrib import admin
from .models import Formar

class FormarAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Formar, FormarAdmin)