from question.models import *
from question.forms import *
from .models import *
from .forms import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import uuid

# Create your views here.
# post answers
@login_required
def view_answers_create(request, pk):
    try: 
        question = Question.objects.get(pk=pk)
        print(question)
    except Question.DoesNotExist:
        return redirect('questions:questions_index')

    
    answer_form = AnswerForm()
    
    if request.method=='POST':
        answer_form = AnswerForm(request.POST, request.FILES)
        if answer_form.is_valid():
            # answer = Answer.objects.create(name=request.user.name,answer=answer, question=question)
            answer = Answer(name=request.user,
                            answer=request.POST['answer'],
                            ansimg=request.FILES['ansimg'],
                            question=question)
            answer.save()

            return redirect('questions:question_show', question.id)
    
    context = {'question': question, 'answer_form': answer_form,}
    return render (request, 'answers/answer_create.html', context)
