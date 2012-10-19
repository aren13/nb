#-*- coding: utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User

##
from choices import *

#def quest_file_upload_to(instance, filename):
#    return '/'.join(['quests', '%Y/%m/%d' , instance.id ,filename])


class Photo(models.Model):
	competitor = models.ForeignKey(User, verbose_name="Yarışmacı")
#	quest  = models.ForeignKey(Quest, verbose_name="Ait olduğu Görev")
	photo = models.ImageField(verbose_name="Fotoğraf", upload_to = 'quest/photos/%Y/%m/%d/')

	def __unicode__(self):
		return u'%s' %self.photo

	def photoname(self):
		return os.path.basename(self.photo.name)

class Quest(models.Model):
	class Meta:
		get_latest_by = 'date'
		ordering = ['-date']

	creator = models.ForeignKey(User, verbose_name="Oluşturan", related_name="oluşturan")
#	competitors = models.ManyToManyField(User, verbose_name="Tamamlayanlar", related_name="tamamlayanlar", null=True, blank=True) 
#	completedQuest = models.ManyToManyField(CompletedQuest, verbose_name="Tamamlayanlar", related_name="tamamlayanlar", null=True, blank=True)
#	photo = models.ImageField(verbose_name="Fotoğraf", upload_to = 'quest/photos/%Y/%m/%d/')
	photo = models.ForeignKey(Photo, verbose_name="Fotoğraf")
	status = models.BooleanField(verbose_name="Yayınlanma durumu" , default=False)
	title = models.CharField(verbose_name="Başlık", max_length=140)
	description = models.TextField(verbose_name="Açıklama", max_length=140, null= True , blank=True)
	country = models.IntegerField(verbose_name="Ülke", null=True, blank=True, choices=COUNTRY_CHOICES) 
	city = models.IntegerField(verbose_name="Şehir", null=True, blank=True, choices=TOWN_CHOICES)
	difficulty = models.IntegerField(verbose_name="Zorluk", null=True, blank=True, choices=DEGREE)
	point = models.IntegerField(verbose_name="Puan", null=True, blank=True)
	date = models.DateField(verbose_name="Tarih" , auto_now_add=True)
	shareOnFacebook = models.BooleanField(verbose_name="Facebook'ta paylaş" , default=True)
#	keywords  = Tag olayı
# 	category = ?

	def __unicode__(self):
		return u'%s' %self.title
		
	def photoName(self):
		photo = self.photo
		return os.path.basename(self.photo.name)

class CompletedQuest(models.Model):
	class Meta:
		get_latest_by=	'date'
		ordering = ['-date']

	quest = models.ForeignKey(Quest, verbose_name="Quest")
	competitor = models.ForeignKey(User, verbose_name="Yarışmacı")
	status = models.BooleanField(verbose_name="Onaylanma durumu" , default=False)		
	photo = models.ForeignKey(Photo, verbose_name="Fotoğraf")	
#	photo = models.ImageField(verbose_name="Photo" , upload_to='quest/photos/%Y/%m/%d/')
	date= models.DateField(verbose_name="Tamamlanma Tarihi", auto_now_add=True)

	def __unicode__(self):
		return u'%s' %self.quest
		
	def photoName(self):
		return os.path.basename(self.photo.name)

