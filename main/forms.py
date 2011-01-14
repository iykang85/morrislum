from django import forms
from main.models import Profile, Resume
from blog.widgets import FCKEditor

class ProfileAdminForm(forms.ModelForm):
    content = forms.CharField(widget=FCKEditor())

    class Meta:
        model = Profile

class ResumeAdminForm(forms.ModelForm):
    content = forms.CharField(widget=FCKEditor())

    class Meta:
        model = Resume 

