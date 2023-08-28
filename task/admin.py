from django.contrib import admin

from .forms import GroupForms
from .models import GroupCourse, Task, Result


# Register your models here.
class GroupCourseAdmin(admin.ModelAdmin):
    form = GroupForms


admin.site.register(GroupCourse, GroupCourseAdmin)
admin.site.register(Task)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('task', 'student', 'result', 'code', 'updated_at', 'is_active')
