from django import forms
from django.forms import widgets
from .models import *

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Post
        field = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description of the problem'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
