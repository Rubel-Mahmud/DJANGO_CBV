from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=400)
    description = forms.CharField(widget=forms.Textarea())


