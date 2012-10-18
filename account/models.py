#-*- coding: utf-8 -*-
from django.db import models
from nb.quest.models import * 
from nb.django_facebook.models import FacebookProfileModel


# Create your models here.
EDUCATION_CHOICES= (('ilk', 'İlköğretim') , ('lise','Lise') , ('onLisans', 'Önlisans'), ('lisans','Lisans'),('yuksek','Yüksek Lisans'),('doktora','Doktora'))
GENDER = ((0, 'Erkek') , (1, 'Kadın'))

class UserProfile(FacebookProfileModel): 
	class Meta:
	    get_latest_by = 'reg_no'
	    
	user = models.OneToOneField(User)

	# Other fields here
	name  = models.CharField(verbose_name="İsim", max_length=50, blank=True, null=True)
	surname = models.CharField(verbose_name="Soyisim", max_length=50, blank=True, null=True)
#	regNo = models.IntegerField(verbose_name="Üye No", max_length=5, unique=True)
	rank  = models.IntegerField(verbose_name="Sıralama", max_length=15, blank=True, null=True)
	point = models.IntegerField(verbose_name="Puan", max_length=15, blank=True, null=True)
	mail = models.EmailField(verbose_name="E-posta adresi",blank=True, null=True)
##	gender = models.IntegerField(verbose_name="Cinsiyet", max_length=2, blank=True, null=True, choices=GENDER )  ##Clashes w/ DJ_FB UserProfile
	town = models.IntegerField(verbose_name="Şehir", max_length=10, blank=True, null=True, choices=TOWN_CHOICES)
	birthdate = models.DateField(verbose_name="Doğum Tarihi",  null=True, blank=True)
	education = models.CharField(verbose_name="Eğitim", max_length=15, blank=True, null=True, choices=EDUCATION_CHOICES)
	website = models.URLField(verbose_name="İnternet sitesi", blank=True, null=True)
	facebook = models.URLField(verbose_name="Facebook Hesabı", blank=True, null=True)
	twitter = models.CharField(verbose_name="Twitter Hesabı",max_length=50 , blank=True , null=True)
	created_quests = models.ManyToManyField(Quest, verbose_name="oluşturduğu maceralar" , null=True, blank=True)
	completed_quests = models.ManyToManyField(CompletedQuest, verbose_name="tamamladığı maceralar" , null=True, blank=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.name , self.surname)


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	"""Create a matching profile whenever a user object is created."""
	if created: 
		profile, new = UserProfile.objects.get_or_create(user=instance)

        
