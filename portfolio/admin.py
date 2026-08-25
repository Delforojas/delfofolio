from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created", "updated")
    list_filter = ("category",)
    search_fields = ("title", "description", "technologies")
    readonly_fields = ("created", "updated")


admin.site.register(Project, ProjectAdmin)
