from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'showpdf.views.index'),
    url(r'^load/$', 'showpdf.views.load_pdf'),
    url(r'^show/(?P<id_pdf>.*)', 'showpdf.views.show_pdf'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)