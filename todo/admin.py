from django.contrib import admin
from .models import Tasks

class TodoAdmin(admin.ModelAdmin):
    readonly_fields =("created",)

admin.site.register(Tasks, TodoAdmin)