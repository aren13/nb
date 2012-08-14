from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'nb.views.home', name='home'),
    # url(r'^nb/', include('nb.foo.urls')),
	url(r'^', include('nb.website.urls')),
	url(r'^', include('nb.account.urls')),
	url(r'^', include('nb.quest.urls')),

	# socialregistration urls
#	url(r'^social/', include('socialregistration.urls',namespace='socialregistration')),     

	# Django_facebook urls
	(r'^facebook/', include('django_facebook.urls')),
#	(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.

	#django-registration urls 
	
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^site_media/?(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }, 'site-media'),
)
