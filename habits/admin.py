from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from .models import Habit, Day


admin.site.register(Habit, SimpleHistoryAdmin)
admin.site.register(Day, SimpleHistoryAdmin)
