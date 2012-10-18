from django.contrib import admin
from models import *

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('competitor', 'photo')

class QuestAdmin(admin.ModelAdmin):
	list_display = ('title', 'creator' , 'date')

class CompletedQuestAdmin(admin.ModelAdmin):
	list_display = ('quest', 'competitor' , 'date') 	
	

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Quest, QuestAdmin)
admin.site.register(CompletedQuest, CompletedQuestAdmin)
