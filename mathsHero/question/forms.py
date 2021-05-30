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

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = '__all__'
#         exclude = ('name', 'question',)

#         widgets = {
#             # 'name': forms.TextInput(attrs={
#             #     'class': 'form-control',
#             #     'placeholder': 'Name'
#             # }),
#             'answer': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Describe your answers here...'
#             }),
#             'ansimg': forms.FileInput(attrs={
#                 'class': 'form-control',
#             }),
#             # 'question': forms.Select(attrs={
#             #     'class': 'form-control'
#             # })
#         }
