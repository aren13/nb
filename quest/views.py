#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import  HttpResponseRedirect
from django.core.urlresolvers import reverse
##
from nb.website.views import r2r
from nb.quest.forms import *



def quest_list(request):
	return r2r(request, 'quest/list.html', {"quest_list":quest_list})


@login_required
#def quest_add(request,reg_no):
def quest_add(request):
#	other_user = get_user(reg_no)
	other_user = request.user
	form = QuestForm(request.POST or None , request.FILES or None)
	if form.is_valid():
		quest = form.save(commit=False)
#		quest.creator = User.objects.get(userprofile=other_user)
		quest.creator = request.user
		quest.status = False
		quest.save()
		other_user.quests.add(quest)
		return HttpResponseRedirect(reverse('quest_list', args=(reg_no,)))
	return r2r(request, 'quest/add.html', {'form': form , "other_user":other_user })

def quest(request , id=None):
#	if id == None;
#	else:
	return r2r(request, 'quest/quest.html', {})

@login_required
def leaderboard(request):
#	user_list = User.objects.all().order_by('rank')
	user_list = User.objects.all()
	return r2r(request, 'quest/leaderboard.html', {"users":user_list})	
