from django import forms

class PostCreateForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=50)
    content = forms.CharField(label='内容', max_length=1000)
    star = forms.IntegerField(label='スター')