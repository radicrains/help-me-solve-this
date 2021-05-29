import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from question.models import Question
from answers.models import Answer
from answers.forms import AnswerForm
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
# book = new Review({ name: name, review: review, book: book })
# book.save()


@login_required
def views_create(request, question):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.save()
            # 1
            # review = Review(name=request.POST['name'], review=request.POST['review'],
            #   book=book)
            # review.save()

            # 2
            question = Question.objects.get(pk=book)
            question.reviews.create(
                name=request.POST['name'], answer=request.POST['answer'])

            return redirect('questions:question_show', question.id)
    return HttpResponse({"message": "works"})


@csrf_exempt
@login_required
def view_reviews(request, question_id):

    if request.method == 'POST':
        # convert data from fetch to dict. json to dict
        # https://www.w3schools.com/python/python_json.asp
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        # find instance of book
        question = Question.objects.get(pk=question_id)
        # use instace of book to save reviews
        question.reviews.create(name=request.user,
                            review=json_data['review'], question=question_id)
        # https://docs.djangoproject.com/en/3.2/ref/request-response/#jsonresponse-objects
        return JsonResponse({"message": "success"}, status=200, safe=True)

    print(request.user.username)
    answers = Answer.objects.filter(
        name=request.user)
    print(answers)
    serialize = [r.serialize() for ans in answers]
    return JsonResponse(serialize, safe=False)
