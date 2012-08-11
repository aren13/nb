#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

##
DEGREE = ((1, "1 - Çok Kolay"), (2, 2) , (3,3), (4,4) , (5,5) , (6,6), (7,7), (8,8), (9,9), (10,"10 - Çok Zor"))

COUNTRY_CHOICES= (
(90 , 'Türkiye' ) ,
)

TOWN_CHOICES= (
(901 , 'Adana' ) ,
(902 , 'Adıyaman') , 
(903 , 'Afyon' ) ,  
(904 , 'Ağrı' ) , 
(905 , 'Amasya') ,
(906 , 'Ankara') ,
(907 , 'Antalya') ,
(908 , 'Artvin') ,
(909 , 'Aydın') ,
(9010 , 'Balıkesir') ,
(9011 , 'Bilecik') ,
(9012 , 'Bingöl') ,
(9013 , 'Bitlis') ,
(9014 , 'Bolu') ,
(9015 , 'Burdur') ,
(9016 , 'Bursa') ,
(9017 , 'Çanakkale') ,
(9018 , 'Çankırı') ,
(9019 , 'Çorum') ,
(9020 , 'Denizli') ,
(9021 , 'Diyarbakır') ,
(9022 , 'Edirne') ,
(9023 , 'Elazığ') ,
(9024 , 'Erzincan') ,
(9025 , 'Erzurum') ,
(9026 , 'Eskişehir') ,
(9027 , 'Gaziantep') ,
(9028 , 'Giresun') ,
(9029 , 'Gümüşhane') ,
(9030 , 'Hakkari') ,
(9031 , 'Hatay') ,
(9032 , 'Isparta') ,
(9033 , 'Mersin') ,
(9034 , 'İstanbul') ,
(9035 , 'İzmir') ,
(9036 , 'Kars') ,
(9037 , 'Kastamonu') ,
(9038 , 'Kayseri') ,
(9039 , 'Kırklareli') ,
(9040 , 'Kırşehir') ,
(9041  , 'Kocaeli') ,
(9042  , 'Konya') ,
(9043  , 'Kütahya') ,
(9044  , 'Malatya') ,
(9045  , 'Manisa') ,
(9046  , 'K.Maraş') ,
(9047  , 'Mardin') ,
(9048  , 'Muğla') ,
(9049  , 'Muş') ,
(9050  , 'Nevşehir') ,
(9051  , 'Niğde') ,
(9052  , 'Ordu') ,
(9053  , 'Rize') ,
(9054  , 'Sakarya') ,
(9055  , 'Samsun') ,
(9056  , 'Siirt') ,
(9057  , 'Sinop') ,
(9058  , 'Sivas') ,
(9059  , 'Tekirdağ') ,
(9060  , 'Tokat') ,
(9061  , 'Trabzon') ,
(9062  , 'Tunceli') ,
(9063  , 'Şanlıurfa') ,
(9064  , 'Uşak') ,
(9065  , 'Van') ,
(9066  , 'Yozgat') ,
(9067  , 'Zonguldak') ,
(9068  , 'Aksaray') ,
(9069  , 'Bayburt') ,
(9070  , 'Karaman') ,
(9071  , 'Kırıkkale') ,
(9072  , 'Batman') ,
(9073  , 'Şırnak') ,
(9074  , 'Bartın') ,
(9075  , 'Ardahan') ,
(9076  , 'Iğdır') ,
(9077  , 'Yalova') ,
(9078  , 'Karabük') ,
(9079  , 'Kilis') ,
(9080  , 'Osmaniye'),
(9081  , 'Düzce')
)

def quest_file_upload_to(instance, filename):
    return '/'.join(['quests', '%Y/%m/%d' , instance.id ,filename])

class Quest(models.Model):
	class Meta:
		get_latest_by = 'date'
		ordering = ['-date']

	creator = models.ForeignKey(User, verbose_name="Oluşturan", related_name="oluşturan")
	competitors = models.ManyToManyField(User, verbose_name="Tamamlayanlar", related_name="tamamlayanlar") 
	status = models.BooleanField(verbose_name="Yayınlanma durumu" , default=False)
	photo = models.ImageField(verbose_name="Tahlil", upload_to =quest_file_upload_to)
	title = models.CharField(verbose_name="Başlık", max_length=120)
	country = models.IntegerField(verbose_name="Ülke", null=True, blank=True, choices=COUNTRY_CHOICES) 
	city = models.IntegerField(verbose_name="Şehir", null=True, blank=True, choices=TOWN_CHOICES)
	description = models.TextField(verbose_name="Açıklama", max_length=200, null= True , blank=True)
	difficulty = models.IntegerField(verbose_name="Zorluk", null=True, blank=True, choices=DEGREE)
#	keywords  = Tag olayı
	shareOnFacebook = models.BooleanField(verbose_name="Facebook'ta paylaş" , default=True)
	point = models.IntegerField(verbose_name="Puan", null=True, blank=True,)
	date = models.DateField(verbose_name="Tarih")

	def photoName(self):
		return os.path.basename(self.photo.name)

class CompletedQuest(models.Model):
	class Meta:
		get_latest_by=	'date'
		ordering = ['-date']
		
	quest = models.ForeignKey(Quest, verbose_name="Quest")
	competitor = models.ForeignKey(User, verbose_name="Kullanıcı")
	photo = models.ImageField(verbose_name="Photo" , upload_to=quest_file_upload_to)
	date= models.DateField(verbose_name="Tarih")

	def photoName(self):
		return os.path.basename(self.photo.name)

