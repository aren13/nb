#-*- coding: utf-8 -*-
from nb.website.models import *
from nb.quest.models import *
from nb.quest.choices import *
from django import forms
import datetime

def global_date(label_name="Tarih"):
	return forms.DateField(label=label_name , input_formats=('%d/%m/%Y', '%d/%m/%Y'), widget=forms.DateInput(format = '%d/%m/%Y'), initial=datetime.date.today, required=True)

def global_hour(label_name="Saat"):
	return forms.DateField(label=label_name , input_formats=('%H:%M', '%H:%M'), widget=forms.DateInput(format = '%H:%M'), initial=datetime.date.today, required=True)

global_attrs={'col':60, 'rows':4}

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
		exclude = ('competitor')

class QuestForm(forms.ModelForm):
	class Meta:
		model = Quest
		exclude = ( 'photo' , 'creator' , 'status' , 'point' , 'date' )
#		fields = ('photo', 'title', 'country', 'city', 'description', 'difficulty', 'shareOnFacebook')
		widgets = {
			'description': forms.Textarea(attrs={'cols':60 , 'rows':4 }),
		}
	
