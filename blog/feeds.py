from django.contrib.syndication.feeds import Feed
from blog.models import Post

class LatestPosts(Feed):
    title = "Morris Lum's Blog"
    link = "/blog/"
    description = "Latest posts on Morris Lum's blog."

    def items(self):
        return Post.objects.order_by('-pub_date')[:10]


