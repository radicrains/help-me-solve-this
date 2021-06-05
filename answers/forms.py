from django import forms
from django.forms import widgets
from .models import *


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        
        widgets = {
            # 'name': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Name'
            # }),
            'answer': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your answers here...'
            }),
            'ansimg': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            # 'question': forms.Select(attrs={
            #     'class': 'form-control'
            # })
        }

        exclude = ('name', 'question',)