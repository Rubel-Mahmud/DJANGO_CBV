from django import forms
from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=400)
    description = forms.CharField(widget=forms.Textarea())


class ArticleCreationForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Article
        fields = ('title', 'body', 'is_public')
