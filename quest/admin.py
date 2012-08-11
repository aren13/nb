from django.contrib import admin
from models import *


admin.site.register(Quest)

class Quest(admin.ModelAdmin):
	list_display = ('title', 'creator')
