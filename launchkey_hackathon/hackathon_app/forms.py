from django import forms
from django.forms import Textarea
from hackathon_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'user')
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }

