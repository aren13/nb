from django.contrib import admin
from models import *

admin.site.register(UserProfile)

class UserProfile(admin.ModelAdmin):
	list_display = ('regNo','rank', 'name', 'surname', 'point')
