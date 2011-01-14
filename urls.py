from django.conf import settings
from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from photologue.models import Gallery
from morrislum.blog.feeds import LatestPosts
from morrislum.main.feeds import LatestGalleries

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'morrislum.main.views.about', name='about'),
    url(r'^cv/$', 'morrislum.main.views.resume', name='cv'),
    url(r'exhibition/(?P<slug>.+)/$', 'morrislum.main.views.exhibition', name='exhibition'),
    url(r'^$', 'morrislum.main.views.index', name='home'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^blog/', include('morrislum.blog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )

feeds = {
    'blog': LatestPosts,
    'gallery': LatestGalleries,
}

urlpatterns += patterns('',
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

urlpatterns += patterns('',
    url(r'^gallery/tag/(?P<tag>[^/]+)/$',
    tagged_object_list, {
        'queryset_or_model': Gallery, 
        'paginate_by': 5, 
        'allow_empty': True,
        'template_name': 'photologue/tag_detail.html',
        'extra_context': {'sample_size':'%s' % getattr(settings, 'GALLERY_SAMPLE_SIZE', 5)},
    }, name='gallery-tag-detail'),
)

urlpatterns += patterns('',
    (r'^', include('photologue.urls')),
)
