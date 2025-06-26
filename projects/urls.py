from django.contrib import admin
from django.urls import path

from . import views
from django.utils.translation import gettext_lazy as _

admin.site.site_header= _('Project Management')
admin.site.site_title= ('Project Management')

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_list'),  # List of projects
    path('project/create', views.ProjectCreateView.as_view(), name='Project_create'),  # Create a new project
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name='Project_update'),  # Edit an existing project
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='Project_delete'),
    path('task/create', views.TaskCreateView.as_view(), name='Task_create'),
    path('task/edit/<int:pk>', views.TaskUpdateView.as_view(), name='Task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='Task_delete'),

    # Delete a task
]
