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
        exclude = ('user',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        # widgets = {
        #     'name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Create New Category'
        #     }),
        #     'question': forms.HiddenInput(),
        # }
        # exclude = ('question',)

# class FiltercatForm(forms.ModelForm):
#     model = Category
#     fields = name
    
    
    
    # widgets = {
    #     'name': forms.Select(choices=filtered_cat)
    # }