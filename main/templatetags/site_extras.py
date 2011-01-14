from django import template
from django.template import resolve_variable
from django.core.urlresolvers import reverse
from morrislum.main.models import Profile, Link, Exhibition
from photologue.models import Gallery

register = template.Library()

@register.inclusion_tag('about.html')
def about():
    p = Profile.objects.all()[0]
    return {'profile': p}

@register.inclusion_tag('links.html')
def links():
    links = Link.objects.all()
    return {'links': links}

@register.inclusion_tag('contacts.html')
def contacts():
    p = Profile.objects.all()[0]
    contacts = p.contact_set.all()
    return {'contacts': contacts}

@register.inclusion_tag('galleries.html')
def galleries():
    galleries = Gallery.objects.filter(is_public=True)
    return {'galleries': galleries}

@register.inclusion_tag('exhibitions.html')
def exhibitions():
    exhibitions = Exhibition.objects.all()
    return {'exhibitions': exhibitions}

