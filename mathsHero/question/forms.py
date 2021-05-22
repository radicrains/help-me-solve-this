from django import forms
from django.forms import widgets
from .models import *


class QuestionForm(forms.ModelForm):

    # cover = forms.FileField(widget=form)
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
                'placeholder': 'Book Title'
            }),
            # 'author': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Book Author'
            # }),
            # 'price': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Book Price',
            #     'type': 'number'
            # }),
            # 'published_year': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Book Author'
            # }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Book Author'
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


# class SeriesForm(forms.ModelForm):
#     class Meta:
#         model = Series
#         fields = '__all__'
