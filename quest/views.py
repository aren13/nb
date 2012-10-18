#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import  HttpResponseRedirect
from django.core.urlresolvers import reverse
##
from nb.website.views import r2r
from nb.quest.forms import *



def quest_list(request):
	quest_list_notApproved = Quest.objects.filter(status = 0)
	quest_list = Quest.objects.filter(status = 1)
	quest_list_all = Quest.objects.all()
	return r2r(request, 'quest/list.html', {"quest_list":quest_list , "quest_list_notApproved":quest_list_notApproved ,"quest_list_all":quest_list_all })


@login_required
#def quest_add(request,reg_no):
def quest_add(request):
#	other_user = get_user(reg_no)
	userProf = request.user.get_profile()
	photo_form = PhotoForm(request.POST or None ,request.FILES or None)
	quest_form = QuestForm(request.POST or None)
	if photo_form.is_valid() and quest_form.is_valid():
		photo = photo_form.save(commit=False)
		photo.competitor = request.user
		photo.save()
		quest = quest_form.save(commit=False)
		quest.photo = photo
		quest.creator = request.user
		quest.status = False
#		quest.status = True
		quest.save()
#		other_user.quests.add(quest)
#		return HttpResponseRedirect(reverse('quest_list', args=(reg_no,)))
		return HttpResponseRedirect(reverse('quest_list'))
	return r2r(request, 'quest/add.html', {'photo_form': photo_form , 'quest_form': quest_form , "userProf":userProf })

def quest(request , id=None):
#	if id == None;
#	else:
	return r2r(request, 'quest/quest.html', {})

@login_required
def leaderboard(request):
#	user_list = User.objects.all().order_by('rank')
	user_list = User.objects.all()
	return r2r(request, 'quest/leaderboard.html', {"users":user_list})	
