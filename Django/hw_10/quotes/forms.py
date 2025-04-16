from django import forms

class AuthorForm(forms.Form):
    fullname = forms.CharField(max_length=255)
    born_date = forms.CharField(max_length=100)
    born_location = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)

class QuoteForm(forms.Form):
    quote = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=255)  # We'll match this with fullname in MongoDB
    tags = forms.CharField(help_text="Comma-separated tags")