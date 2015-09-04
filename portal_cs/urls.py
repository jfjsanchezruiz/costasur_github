from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal_cs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'principal.views.home', name='home'),
    url(r'^es/$', 'principal.views.home', name='home'),
    url(r'^es/home/$', 'principal.views.home', name='home'),    
    url(r'^es/about/$', 'principal.views.about', name='home'),
    url(r'^es/attractives/$', 'principal.views.attractive', name='home'),
    url(r'^es/products/$', 'principal.views.products', name='home'),
    url(r'^es/news/$', 'principal.views.news', name='home'),
    url(r'^es/contact/$', 'principal.views.contact', name='home'),
    url(r'^es/products/maintenance/$', 'principal.views.maintenance', name='home'),
    url(r'^es/products/telecom/$', 'principal.views.telecom', name='home'),
    url(r'^es/products/legal/$', 'principal.views.legal', name='home'),
    url(r'^es/products/access/$', 'principal.views.access', name='home'),
    url(r'^es/products/lrcc/$', 'principal.views.lrcc', name='home'),    
    url(r'^es/news/cccn/$', 'principal.views.cccn', name='home'),
    url(r'^es/news/qpasa/$', 'principal.views.qpasa', name='home'),
    url(r'^es/news/cdcliving/$', 'principal.views.cdcliving', name='home'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'portal_cs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'principal.views.home', name='home'),
    url(r'^en/$', 'principal.views.home', name='home'),
    url(r'^en/home/$', 'principal.views.home', name='home'),    
    url(r'^en/about/$', 'principal.views.about', name='home'),
    url(r'^en/attractives/$', 'principal.views.attractive', name='home'),
    url(r'^en/products/$', 'principal.views.products', name='home'),
    url(r'^en/news/$', 'principal.views.news', name='home'),
    url(r'^en/contact/$', 'principal.views.contact', name='home'),
    url(r'^en/products/maintenance/$', 'principal.views.maintenance', name='home'),
    url(r'^en/products/telecom/$', 'principal.views.telecom', name='home'),
    url(r'^en/products/legal/$', 'principal.views.legal', name='home'),
    url(r'^en/products/access/$', 'principal.views.access', name='home'),
    url(r'^en/products/lrcc/$', 'principal.views.lrcc', name='home'),   
    url(r'^en/news/cccn/$', 'principal.views.cccn', name='home'),
    url(r'^en/news/qpasa/$', 'principal.views.qpasa', name='home'),
    url(r'^en/news/cdcliving/$', 'principal.views.cdcliving', name='home'),         
)
