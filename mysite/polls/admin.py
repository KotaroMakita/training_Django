from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Choice,Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['questino_text']}),
        ('Date information',{'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)


