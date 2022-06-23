from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from .models import Habit, Profile, Day


admin.site.register(Habit, SimpleHistoryAdmin)
admin.site.register(Profile, SimpleHistoryAdmin)
admin.site.register(Day, SimpleHistoryAdmin)
