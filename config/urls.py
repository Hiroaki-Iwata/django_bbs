from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from thread.sitemaps import TopicSitemap, CategorySitemap
from base.sitemaps import BaseSitemap
from django.conf.urls.static import static

sitemaps = {
    'topic': TopicSitemap,
    'category': CategorySitemap,
    'base': BaseSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('base.urls')),
    path('thread/', include('thread.urls')),
    path('api/', include('api.urls')),
    path('search/', include('search.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns