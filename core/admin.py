from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from .models import Profile


admin.site.register(Profile, SimpleHistoryAdmin)
