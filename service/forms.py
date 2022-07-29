from django.forms import ModelForm, fields, widgets
from .models import Post, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
