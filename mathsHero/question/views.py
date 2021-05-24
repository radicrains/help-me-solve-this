# from question.models import Category, Question
# from question.forms import CategoryForm, QuestionForm

from question.models import *
from question.forms import *
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
                        cover=request.FILES['cover'])

            question.save()
            categories = form.cleaned_data['categories']

            for cat in categories:
                question.categories.add(cat)

            return redirect('questions:questions_index')
    
    questions = Question.objects.all()
    context = {"form": form, "questions": questions}
    
     # posts = Post.objects.filter(hidden=False).order_by('-created_at')
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

    # review_form = ReviewForm()
    # print(review_form)
    # context = {"question": question, "edit": False, "review_form": review_form}
    context = {"question": question, "edit": False}
    return render(request, 'question/show.html', context)

