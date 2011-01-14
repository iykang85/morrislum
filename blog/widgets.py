from django.forms import *
from django.forms.widgets import flatatt
from django.forms.util import smart_unicode
from django.utils.html import escape
from django.utils.simplejson import *
from django.utils.safestring import mark_safe
from django.conf import settings
        
class FCKEditor(Textarea):
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs, name=name)
        base_path = '%sjs/fckeditor/' % settings.MEDIA_URL
        
        return mark_safe(u'''
            <textarea%s>%s</textarea>
            <script type="text/javascript">
                var oFCKeditor = new FCKeditor("%s");
                oFCKeditor.BasePath = "%s";
                oFCKeditor.Height = '500';
                oFCKeditor.ReplaceTextarea();
            </script>


        ''' % (flatatt(final_attrs), escape(value), name, base_path))
        
