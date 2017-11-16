from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views
from tags import views as tags_views
from images import views as images_views
from posts.feeds import ArticlesRSSFeed, ArticlesAtomFeed

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^console/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^tags/$', tags_views.show_tags, name='tags'),
    url(r'^tag/([0-9]+)/$', tags_views.show_tagged_figures, name='tagged_figures'),
    url(r'^images/$', images_views.show_images, name='images'),
    url(r'^images/([0-9]+)/$', images_views.show_image, name='show_image'),
    url(r'^rss/a/$', ArticlesRSSFeed()),
    url(r'^atom/a/$', ArticlesAtomFeed()),
    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
