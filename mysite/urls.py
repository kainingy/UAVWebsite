from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', 'myapp.views.index', name = 'index'),
    url(r'^blog/','myapp.views.home', name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<id>\d+)/$', 'myapp.views.detail', name='detail'),
    url(r'^archives/$', 'myapp.views.archives', name = 'archives'),
    url(r'^tag(?P<tag>\w+)/$', 'myapp.views.search_tag', name = 'search_tag'),
    url(r'^contact/thanks', 'myapp.views.thankyou'),
    url(r'^contact/', 'myapp.views.contactview'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^gallery/', 'myapp.views.galleryView'),
)+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)