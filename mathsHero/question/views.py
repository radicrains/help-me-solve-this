# from question.models import Category, Question
# from question.forms import CategoryForm, QuestionForm

from question.models import *
from question.forms import *
from answers.models import *
# from answers.forms import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import uuid
# Create your views here.

@login_required
def view_question_create(request):
    qns_form = QuestionForm()

    if request.method == 'POST':
        qns_form = QuestionForm(request.POST, request.FILES)
        if qns_form.is_valid():

            question = Question(title=request.POST['title'],
                        description=request.POST['description'], 
                        cover=request.FILES['cover'],
                        user=request.user)
            question.save()

            categories = qns_form.cleaned_data['categories']
            for cat in categories:
                question.categories.add(cat)

            return redirect('questions:questions_index')

    context = {"form": qns_form,} 
    return render(request, 'question/qn_create.html', context)

@login_required
def view_index(request):
    
    #filter qn by category selection
    questions = Question.objects.all() 
    categories = Category.objects.all()

    filtered_cat = request.GET.get("category_filter") 

    if filtered_cat != '' and filtered_cat is not None: 
        print(filtered_cat)
        questions = questions.filter(categories__name=filtered_cat) 

    context = {"questions":questions, "categories":categories} 
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

    
    qn_answers = Answer.objects.filter(question_id=pk)
    # print(qn_answers)

    context = {"question": question, 'answers':qn_answers, "edit": False}
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



# # post answers
# @login_required
# def view_answers_create(request, pk):
#     try: 
#         question = Question.objects.get(pk=pk)
#         print(question)
#     except Question.DoesNotExist:
#         return redirect('questions:questions_index')

    
#     answer_form = AnswerForm()
    
#     if request.method=='POST':
#         answer_form = AnswerForm(request.POST, request.FILES)
#         if answer_form.is_valid():
#             # answer = Answer.objects.create(name=request.user.name,answer=answer, question=question)
#             answer = Answer(name=request.user,
#                             answer=request.POST['answer'],
#                             ansimg=request.FILES['ansimg'],
#                             question=question)
#             answer.save()

#             return redirect('questions:question_show', question.id)

#         # answer = Answer.objects.filter(question__id=pk)
#         # print(answer)

#     # context = {'question': question, 'answer': answer, 'answer_form': answer_form,}
#     context = {'question': question, 'answer_form': answer_form,}
#     return render (request, 'question/answer_create.html', context)
