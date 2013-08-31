from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('collage.collageapp.views',
    # Examples:
    url(r'^$', 'home'),
    url(r'^create/$', 'create_collage'),
    url(r'^collages/$', 'collages_list'),
    url(r'^collage/(?P<c_id>\d+)/$', 'collage_details'),    

    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
