from django.contrib import admin
from .models import Priority, Tag, DayTask, IntervalTask, SimpleTask

# Register your models here.
admin.site.register(Priority)
admin.site.register(Tag)
admin.site.register(DayTask)
admin.site.register(IntervalTask)
admin.site.register(SimpleTask)
