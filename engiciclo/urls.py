from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
#     (r'^engiciclo/', include('engiciclo.foo.urls')),
     (r'^empresas/$', 'crm.views.index'),
#     (r'^empresas/(?P<empresa_id>\d+)/$', 'crm.views.detail'),


    # Uncomment the admin/doc line below to enable admin documentation:
#     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),

    #static
    (r'^media2/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/workspace/django/engiciclo/media'}),
)
