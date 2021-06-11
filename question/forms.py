from django import forms
from django.forms import widgets
from .models import *


class QuestionForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Question Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description of the problem'
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'user': forms.HiddenInput(),
        }
        exclude = ('user','likes')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
