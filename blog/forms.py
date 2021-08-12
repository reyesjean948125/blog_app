from django import forms
from .models import Post

class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = "__all__"

class CommentForm(forms.Form):
	author = forms.CharField(
		max_length=60,
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Your Name"
		})
	)
	body = forms.CharField(widget=forms.Textarea(
		attrs={
			"class": "form-control",
			"placeholder": "Leave a comment!"
		})
	)