# from question.models import Category, Question
# from question.forms import CategoryForm, QuestionForm

from question.models import *
from question.forms import *
# from answers.forms import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import uuid
# Create your views here.

@login_required
def view_index(request):
    
    form = QuestionForm()
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():

            question = Question(title=request.POST['title'],
                        description=request.POST['description'], 
                        cover=request.FILES['cover'],
                        user=request.user)
            question.save()

            categories = form.cleaned_data['categories']
            for cat in categories:
                question.categories.add(cat)

            return redirect('questions:questions_index')
    
    #filter qn by category selection
    questions = Question.objects.all() 
    filtered_cat = request.GET.get("category_filter") 

    if filtered_cat != '' and filtered_cat is not None: 
        print(filtered_cat)
        questions = questions.filter(categories__name=filtered_cat) 

    
    categories = Category.objects.all() 
    context = {"form": form, "questions":questions, "categories":categories} 
    
    return render(request, 'question/index.html', context)


@login_required
def view_show(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return redirect('questions:questions_index')

    if request.GET.get('action') == 'del':
        question.delete()
        return redirect('questions:questions_index')


    if request.method == 'POST' and request.GET['action'] == 'edit':
        print("i am here")
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions:question_show', question.id)

    if request.GET.get('action') == 'edit':
        form = QuestionForm(instance=question)
        context = {"question": question, "edit": True, "form": form}
        return render(request, 'question/show.html', context)

    # answers_form = AnswerForm()
    # print(answers_form)
    # context = {"question": question, "edit": False, "answers_form": answers_form}
    context = {"question": question, "edit": False}
    return render(request, 'question/show.html', context)


@login_required
def view_category_create(request):

    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category = Category(name=request.POST['name'])

            category_form.save()
            return redirect('questions:questions_index')
    context = {"category_form": category_form}
    return render(request, 'question/category.html', context)

