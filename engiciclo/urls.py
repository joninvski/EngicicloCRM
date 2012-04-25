from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^poster/$', 'crm.views.index'),
#     (r'^recolhas/(?P<empresa_id>\d+)/$', 'crm.views.recolhas_single'),
     (r'^$', redirect_to, {'url': '/ist/crm/poster/add'}),
     (r'^admin/', include(admin.site.urls)),
     (r'^crm/$', redirect_to, {'url': '/admin/crm'}),
     (r'^crm/$', 'crm.views.confirmacao'),

     (r'^ist/crm/poster[/]$', redirect_to, {'url': '/ist/crm/poster/add'}),
     (r'^ist/confirmacao/$', 'crm.views.confirmacao'),

     (r'^ist/$', redirect_to, {'url': '/ist/crm/poster/add'}),
     (r'^ist/crm/$', redirect_to, {'url': '/ist/confirmacao/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
#     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^ist/', include(admin.site.urls)),

    #static
    (r'^photos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/cnm/jtrindade/posters/photos'}),
)
