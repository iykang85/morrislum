from django.conf import settings
from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from blog.models import *

# galleries
blog_args = {
    'date_field': 'pub_date', 
    'allow_empty': True, 
    'queryset': Post.objects.all().order_by('-pub_date'), 
    'extra_context': {'months': Post.objects.dates('pub_date', 'month')}
}

blog_month_args = {
    'month_format': '%m',
}
blog_month_args.update(blog_args)


urlpatterns = patterns('django.views.generic.date_based',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\-\d\w]+)/$', 'object_detail', {
        'month_format': '%m',
        'date_field': 'pub_date', 
        'queryset': Post.objects.all(), 
        'extra_context': {'months': Post.objects.dates('pub_date', 'month')}
    }, name='blog-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day', blog_month_args, name='blog-archive-day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', blog_month_args, name='blog-archive-month'),
    url(r'^(?P<year>\d{4})/$', 'archive_year', blog_args, name='blog-archive-year'),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^page/(?P<page>[0-9]+)/$', 'object_list', {
        'queryset': Post.objects.all().order_by('-pub_date'), 
        'allow_empty': True, 
        'paginate_by': 5,
        'extra_context': {'months': Post.objects.dates('pub_date', 'month')}
    }, name='blog-list'),
    url(r'^$', 'object_list', {
        'queryset': Post.objects.all().order_by('-pub_date'), 
        'allow_empty': True, 
        'paginate_by': 5,
        'page': 1,
        'extra_context': {'months': Post.objects.dates('pub_date', 'month')}
    },name='blog-list-index'),
)

urlpatterns += patterns('',
    url(r'^tag/(?P<tag>[^/]+)/$',
    tagged_object_list, {
        'queryset_or_model': Post, 
        'paginate_by': 5, 
        'allow_empty': True,
        'template_name': 'blog/tag_detail.html',
        'extra_context': {'months': Post.objects.dates('pub_date', 'month')}
    }, name='blog-tag-detail'),
)



