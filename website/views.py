# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from nb.website.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.utils import simplejson
import urllib2

def r2r(request, v, c, mimetype="text/html"):
	return render_to_response(v,c, context_instance=RequestContext(request), mimetype=mimetype)

def home(request):
	return r2r(request, 'home.html', {})
	

def about(request):
	return r2r(request, 'about.html', {})


def faq(request):
	return r2r(request, 'faq.html', {})

def help(request):
	return r2r(request, 'help.html', {})


