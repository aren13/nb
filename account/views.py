# Create your views here.


@login_required
def myboard(request):
	user = request.user
	return r2r(request, 'profile/profile.html', {"user":user })

	
@login_required
def board(request, reg_no):#=None
	user = request.user
	other_user = get_user(reg_no)
#	other_user = User.objects.get(user)
#	bmis = other_user.bmis.all()[:8]
#	meetings = other_user.meetings.all()[:3]
#	health_status = other_user.health_status.filter(client = other_user.user)[:2]
#	return r2r(request, 'profile/board.html', {"bmis":bmis,"meetings":meetings, 'health_status':health_status, 'other_user':other_user, "user":user , "diet":diet})
	return r2r(request, 'profile/board.html', {"user":user})

