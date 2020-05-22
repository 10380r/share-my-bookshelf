from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    CHOICE = [
        ('1', 'business'),
        ('2', 'history'),
        ('3', 'teqcnology'),
    ]
    label = forms.fields.ChoiceField(
        required=True,
        choices = CHOICE,
        widget=forms.Select(attrs={'id':'one'}))
    class Meta:
        model = Post
        fields = ['username', 'isbn_code', 'review', 'star', 'was_read',]