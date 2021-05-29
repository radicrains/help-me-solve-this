from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'ans_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your answers here...'
            }),
            'ans_cover': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'question': forms.Select(attrs={
                'class': 'form-control'
            })
        }
