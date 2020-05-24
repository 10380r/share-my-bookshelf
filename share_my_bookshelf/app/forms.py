from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    CHOICE = [
        ('business', 'business'),
        ('history', 'history'),
        ('technology', 'technology')
    ]
    label = forms.fields.ChoiceField(
        required=False,
        choices = CHOICE,
        widget=forms.Select)
    class Meta:
        model = Post
        fields = ['username', 'isbn_code', 'review', 'star', 'was_read',]