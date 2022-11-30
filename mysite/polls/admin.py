from django.contrib import admin

from .models import Choice, Question

# Defined number of choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# class that keeps all the information about the questions the admin creates
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # set text of question
        (None,               {'fields': ['question_text']}),
        # set date of creation
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # create choices of answer
    inlines = [ChoiceInline]
    # list details about the question creation
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list per date
    list_filter = ['pub_date']
    # search a specific question by question name
    search_fields = ['question_text']

# admin interface
admin.site.register(Question, QuestionAdmin)