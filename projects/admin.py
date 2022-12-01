from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created')
    fields = ('id', 'created', 'title', 'description')


admin.site.register(models.Project, ProjectAdmin)
