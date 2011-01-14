from django.contrib.comments.moderation import CommentModerator, moderator
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from photologue.models import Gallery

class Profile(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return '/about/'

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField('e-mail address')
    profile = models.ForeignKey(Profile)

    def __unicode__(self):
        return self.email

class Link(models.Model):
    title = models.CharField('title', max_length=100)
    url = models.URLField('URL', max_length=255)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField('CV content')
    pdf = models.FileField('PDF', upload_to='cv', help_text='PDF copy of your CV', blank=True)

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV'

    def get_absolute_url(self):
        return '/resume/'

    def __unicode__(self):
        return self.name

class Exhibition(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField()
    url = models.URLField('URL', max_length=255, help_text='URL to the exhibition')
    description = models.TextField(blank=True, help_text='If left blank, footer link will be external instead of a copy page.')

    def get_absolute_url(self):
        return '/exhibition/%s/' % self.slug

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)

class GalleryModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'date_added'
    moderate_after = 14

    def check_spam(self, request, comment, key, blog_url=None, base_url=None):
        from akismet import Akismet

        if blog_url is None:
            blog_url = 'http://%s/' % Site.objects.get_current().domain

        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url=blog_url
        )

        if base_url is not None:
            ak.baseurl = base_url

        if ak.verify_key():
            data = {
                'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'referrer': request.META.get('HTTP_REFERER', ''),
                'comment_type': 'comment',
                'comment_author': comment.user_name.encode('utf-8'),
            }

            if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
                return True

        return False

    def allow(self, comment, content_object, request):
        allow = super(GalleryModerator, self).allow(comment, content_object, request)

        # change this depending on which spam provider you want to use
        spam = self.check_spam(request, comment, key=settings.AKISMET_API_KEY)
        return not spam and allow


moderator.register(Gallery, GalleryModerator)

