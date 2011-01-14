from django.shortcuts import render_to_response
from django.template import RequestContext 
from photologue.models import Gallery
from morrislum.blog.models import Post
from models import Profile, Resume, Exhibition

def index(request):
    latest_post = None 
    latest_gallery = None
    
    latest_gallery = Gallery.objects.filter(is_public=True)[0:1].get()
    latest_post = Post.objects.order_by('-pub_date')[0:1].get()

    return render_to_response('index.html', {
        'latest_gallery': latest_gallery,
        'latest_post': latest_post,
    }, context_instance=RequestContext(request))

def about(request):
    p = Profile.objects.all()[0:1].get()

    return render_to_response('about_detail.html', {
        'profile': p.content,
    }, context_instance=RequestContext(request))

def resume(request):
    r = Resume.objects.all()[0:1].get()

    return render_to_response('resume_detail.html', {
        'resume': r,
    }, context_instance=RequestContext(request))

def exhibition(request, slug):
    e = Exhibition.objects.filter(slug=slug)[0:1].get()

    return render_to_response('exhibition_detail.html', {
        'exhibition': e,
    }, context_instance=RequestContext(request))

