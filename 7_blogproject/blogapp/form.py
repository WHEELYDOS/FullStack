from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(form.ModelForm):
    class Meta:
        model = Post
        fields =  ['title','content','image']