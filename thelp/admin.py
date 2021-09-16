from django.contrib.admin import ModelAdmin, site

from thelp.models import Task, Comment


class TaskAdmin(ModelAdmin):
    list_display = ["appeal", "room", "person"]


class CommentAdmin(ModelAdmin):
    list_display = ["comment"]


site.register(Comment)
site.register(Task)
