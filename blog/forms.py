from django import forms
from blog.models import Post
from blog.widgets import FCKEditor

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=FCKEditor())

    class Meta:
        model = Post
