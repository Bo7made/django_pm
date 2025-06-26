from django.contrib import admin
from django.db.models import Count
from . import models

# Register models directly
admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_at', 'tasks_count']
    list_per_page = 10
    list_select_related = ['user', 'category']
    list_editable = ['status']

    def get_queryset(self, request):
        query = super().get_queryset(request)
        return query.annotate(tasks_count=Count('task'))  # use 'task' as no related_name is set

    def tasks_count(self, obj):
        return obj.tasks_count

    tasks_count.short_description = 'Number of Tasks'

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 20

