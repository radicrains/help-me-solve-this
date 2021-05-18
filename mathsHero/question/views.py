# from question.models import Category, Question
# from question.forms import CategoryForm, QuestionForm

from question.models import *
from question.forms import *
from django.shortcuts import redirect, render
# from django.contrib.auth.decorators import login_required
import uuid
# Create your views here.


# @login_required
def view_index(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save() can save form data directly

            """
             Save using the Book model
            """
            question = Question(title=request.POST['title'],
                        # author=request.POST['author'],
                        # price=request.POST['price'],
                        description=request.POST['description'], 
                        # published_year=request.POST['published_year'],
                        cover=request.FILES['cover'])

            question.save()
            categories = form.cleaned_data['categories']
            # one line solution to loop below
            # book.categories.add(*categories)
            for cat in categories:
                question.categories.add(cat)
    #

            return redirect('questions: questions_index')
    
    questions = Question.objects.all()
    context = {"form": form, "questions": questions}
    
    return render(request, 'questions/index.html', context)


# @login_required
# def view_show(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return redirect('books:books_index')

#     """
#         Only hits this when the url has ?action=del and a GET request
#     """
#     if request.GET.get('action') == 'del':
#         book.delete()
#         return redirect('books:books_index')

#     """
#         Only hits this when the url has ?action=edit and a POST request
#     """

#     if request.method == 'POST' and request.GET['action'] == 'edit':
#         print("i am here")
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('books:book_show', book.id)

#     """
#         Only hits this when the url has ?action=edit and a GET request
#         this will display the form.
#     """
#     if request.GET.get('action') == 'edit':
#         form = BookForm(instance=book)
#         context = {"book": book, "edit": True, "form": form}
#         return render(request, 'books/show.html', context)

#     review_form = ReviewForm()
#     print(review_form)
#     context = {"book": book, "edit": False, "review_form": review_form}
#     return render(request, 'books/show.html', context)


# @login_required
# def view_create_category(request):

#     category_form = CategoryForm()
#     if request.method == 'POST':
#         category_form = CategoryForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return redirect('books:books_index')
#     context = {"category_form": category_form}
#     return render(request, 'books/create_category.html', context)


# @login_required
# def view_create_series(request):
#     form = SeriesForm()
#     if request.method == 'POST':
#         form = SeriesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # series = Series(name=request.POST['name'],book=request.POST['book'])
#             # series.save()

#             # Series.objects.create(name=request.POST['name'],book=request.POST['book'])
#             return redirect('books:series_create')

#     series = Series.objects.all()
#     context = {"series": series, "form": form}
#     return render(request, 'books/series.html', context)


# def view_series(request, pk):
#     pass
