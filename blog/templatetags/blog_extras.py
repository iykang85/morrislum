from django import template
from django.template import resolve_variable
from django.core.urlresolvers import reverse
from blog.models import BlogrollLink

register = template.Library()

@register.inclusion_tag('blog/blogroll.html')
def blogroll():
    links = BlogrollLink.objects.all()
    return {'links': links}
