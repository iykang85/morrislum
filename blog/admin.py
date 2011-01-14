from django.contrib import admin
from models import Post, BlogrollLink
from forms import PostAdminForm

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'pub_date', 'blurb',)
    list_filter = ('pub_date',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

class BlogrollLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
admin.site.register(BlogrollLink, BlogrollLinkAdmin)


