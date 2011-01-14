from django.contrib.syndication.feeds import Feed
from photologue.models import Gallery

class LatestGalleries(Feed):
    title = "Morris Lum's Galleries"
    link = "/gallery/page/1/"
    description = "Latest galleries on Morris Lum's website."

    def items(self):
        return Gallery.objects.filter(is_public=True)[0:10]



