from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Choice,Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['questino_text']}),
        ('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('questino_text','pub_date','was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['questino_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)


