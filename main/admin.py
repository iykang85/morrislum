from django.contrib import admin
from models import *
from forms import ProfileAdminForm, ResumeAdminForm

class ContactInline(admin.TabularInline):
    model = Contact 

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    inlines = [ContactInline,]
admin.site.register(Profile, ProfileAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
admin.site.register(Link, LinkAdmin)

class ResumeAdmin(admin.ModelAdmin):
    form = ResumeAdminForm 
admin.site.register(Resume, ResumeAdmin)

class ExhibitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Exhibition, ExhibitionAdmin)
