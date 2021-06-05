from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "cover",)


admin.site.register(Question, QuestionAdmin)

admin.site.register(Category)