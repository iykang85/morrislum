from django import forms
from models import Post
from widgets import FCKEditor

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=FCKEditor())

    class Meta:
        model = Post
