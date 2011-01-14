from django.db import models
from django.contrib.comments.moderation import CommentModerator, moderator
from django.utils.html import strip_tags
import tagging
from tagging.fields import TagField
from datetime import datetime
from django.conf import settings
from django.contrib.sites.models import Site

class Post(models.Model):
    title = models.CharField('title', max_length=100, unique=True)
    slug = models.SlugField('slug')
    pub_date = models.DateTimeField('published date', default=datetime.now)
    tags = TagField(help_text='Separate tags with spaces, put quotes around multiple-word tags.', verbose_name='tags')
    content = models.TextField('post content')
    enable_comments = models.BooleanField(default=True)

    def get_absolute_url(self):
        return '/blog/%s/%s/' % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)

    def blurb(self):
        return '%s...' % strip_tags(self.content)[:50]

    def __unicode__(self):
        return self.title

class PostModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'
    auto_moderate_field = 'pub_date'
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
        allow = super(PostModerator, self).allow(comment, content_object, request)

        # change this depending on which spam provider you want to use
        spam = self.check_spam(request, comment, key=settings.AKISMET_API_KEY)
        return not spam and allow

#moderator.register(Post, PostModerator)

class BlogrollLink(models.Model):
    title = models.CharField('title', max_length=100)
    url = models.URLField('URL', max_length=255)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)


