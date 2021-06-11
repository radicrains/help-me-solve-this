from django.contrib import admin
from .models import *

# Register your models here.
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ("name", "answer", "ansimg","question","likes")


admin.site.register(Answer)