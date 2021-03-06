#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import  HttpResponseRedirect
from django.core.urlresolvers import reverse
##
from website.views import r2r
from forms import *
from account.models import UserProfile


def quest_list(request):
	userProf = UserProfile.objects.get(user=request.user)
	quest_list_notApproved = Quest.objects.filter(status = 0)
	quest_list = Quest.objects.filter(status = 1)
	quest_list_all = Quest.objects.all()
	return r2r(request, 'quest/list.html', {"user":userProf ,
	                                        "quest_list":quest_list ,
	                                        "quest_list_notApproved":quest_list_notApproved ,
	                                        "quest_list_all":quest_list_all })


def quest(request , id):
	user = request.user
	userProf = UserProfile.objects.get(user=user)
	quest= Quest.objects.get(id=id)
	completed_quests = CompletedQuest.objects.filter(quest_id=id)
	return r2r(request, 'quest/quest.html', {"user":userProf , "quest":quest ,
	                                         "completed_quests":completed_quests})


@login_required()
def leaderboard(request):
#	user_list = User.objects.all().order_by('rank')
	user_list = UserProfile.objects.all().order_by('rank')
	userProf = UserProfile.objects.get(user=request.user)
	return r2r(request, 'quest/leaderboard.html', {"users":user_list , "user":userProf})


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
	return r2r(request, 'quest/add.html', {'photo_form': photo_form , 'quest_form': quest_form , "user":userProf })

@login_required
#def quest_add(request,reg_no):
def quest_complete(request , id):
#	other_user = get_user(reg_no)
	userProf = request.user.get_profile()
	quest = Quest.objects.get(id=id)
	photo_form = PhotoForm(request.POST or None ,request.FILES or None)
	quest_complete_form = QuestCompleteForm(request.POST or None)
	if photo_form.is_valid() and quest_complete_form.is_valid():
		photo = photo_form.save(commit=False)
		photo.competitor = request.user
		photo.save()
		qc = quest_complete_form.save(commit=False)
		qc.quest = quest
		qc.photo = photo
		qc.competitor = request.user
		qc.status = False
		qc.save()
#		other_user.quests.add(quest)
#		return HttpResponseRedirect(reverse('quest_list', args=(reg_no,)))
		return HttpResponseRedirect(reverse('quest_list'))
	return r2r(request, 'quest/complete.html', {'photo_form': photo_form , 'quest_complete_form': quest_complete_form ,
	                                            "user":userProf})

