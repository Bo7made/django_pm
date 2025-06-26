from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')


class ProjectStatus(models.IntegerChoices):
    PENDING = 1, 'pending'
    COMPLETED = 2, 'completed'
    POSTPONED = 3, 'postponed'
    CANCELED = 4, 'canceled'


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(
        choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    class Meta:
        verbose_name = _('Projects')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

