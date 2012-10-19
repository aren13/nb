# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404
from models import UserProfile
from website.views import r2r

def get_user(reg_no):
	return get_object_or_404(UserProfile, id=reg_no)


@login_required
def myboard(request):#=None
	user = request.user
	userProf = UserProfile.objects.get(user=user)
#	other_user = User.objects.get(user)
#	bmis = other_user.bmis.all()[:8]
#	meetings = other_user.meetings.all()[:3]
#	health_status = other_user.health_status.filter(client = other_user.user)[:2]
#	return r2r(request, 'profile/board.html', {"bmis":bmis,"meetings":meetings, 'health_status':health_status, 'other_user':other_user, "user":user , "diet":diet})
	return r2r(request, 'profile/board.html', {"user":userProf})
	
@login_required
def board(request, reg_no):#=None
	user = request.user
	other_user = get_user(reg_no)
	userProf = UserProfile.objects.get(user=user)
	otherProf = UserProfile.objects.get(user=other_user)
#	other_user = User.objects.get(user)
#	bmis = other_user.bmis.all()[:8]
#	meetings = other_user.meetings.all()[:3]
#	health_status = other_user.health_status.filter(client = other_user.user)[:2]
#	return r2r(request, 'profile/board.html', {"bmis":bmis,"meetings":meetings, 'health_status':health_status, 'other_user':other_user, "user":user , "diet":diet})
	return r2r(request, 'profile/board.html', {"user":userProf, "other_user":otherProf})

