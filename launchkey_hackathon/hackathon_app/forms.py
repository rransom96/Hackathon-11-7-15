from django import forms
from django.forms import Textarea
from hackathon_app.models import Post, Issue, SubComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subissue_rel','title',)
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }


class SubCommentForm(forms.ModelForm):
    class Meta:
        model = SubComment
        fields = ('user','comment_rel','comment_text',)
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('name',)
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }

