from question.models import *
from question.forms import *
from answers.models import *
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
import uuid
# Create your views here.

@login_required
def view_question_create(request):
    qns_form = QuestionForm()
    template_name='question/qn_create.html'

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
    return render(request, template_name, context)

# @login_required
def view_index(request):
    
    #filter qn by category selection
    questions = Question.objects.order_by('-created_at')
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
    
    total_likes = question.total_likes()

    liked = False
    if question.likes.filter(id=request.user.id).exists():
        liked = True
    

    context = {"question": question, 'answers':qn_answers, "edit": False, "total_likes":total_likes, "liked":liked}
    return render(request, 'question/show.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/login/', redirect_field_name='/posts/')
def view_category(request):

    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category = Category(name=request.POST['name'])
            category_form.save()

            return redirect('questions:category')
    
    categories = Category.objects.all()

    context = {"category_form": category_form, "categories":categories}
    return render(request, 'question/category.html', context)


def like_qns(request, pk):
    question = get_object_or_404(Question, id=request.POST.get('qns_id'))
    liked = False
    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
        liked = False
    else:
        question.likes.add(request.user)
        liked = True

    return redirect('questions:question_show', question.id)

