from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'isbn_code', 'review',
        'label', 'star', 'was_read',]
