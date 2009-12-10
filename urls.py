from django.conf.urls.defaults import *
# So we can find our hello world views
from doodle.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myDjangoProject01/', include('myDjangoProject01.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    # For our hello world view
    (r'^helloWorld/', helloWorld),
    # For our hello person view
    (r'^helloPerson/(?P<thePerson>[a-zA-Z]+)/$', helloPerson),
    # For our list doodle type view
    (r'^listDoodleTypes/', listDoodleTypes),
    # For our show doodle type view
    (r'^showDoodleType/(?P<theId>\d)/$', showDoodleType),
    # For our delete doodle type view
    (r'^deleteDoodleType/(?P<theId>\d)/$', deleteDoodleType),
    # For our create doodle type view
    (r'^createDoodleType/(?P<theName>[a-zA-Z]+)/$', createDoodleType),
    # For our update doodle type view
    (r'^updateDoodleType/(?P<theId>\d)/(?P<theName>[a-zA-Z]+)/$', updateDoodleType),
)
