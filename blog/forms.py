from django import forms
from .models import Blog

class BlogCreationForm(forms.ModelForm):
    """ A form to create a blog """
    class Meta:
        model = Blog
        fields = ['title', 'text']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 300px;'}),
        }
        
class BlogUpdateForm(forms.ModelForm):
    """ A form to update a blog """
    class Meta:
        model = Blog
        fields = ['title', 'text']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 300px;'}),
        }
