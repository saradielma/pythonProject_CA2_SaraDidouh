import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

""" Create models so that Django can create a database schema for this app and
create a Python database-access API for accessing Question and Choice objects."""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # resturns question text
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    # check if question was created more than a day ago
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

""" Class choice with its variables to keep the chosen answer (choice), number 
of votes and question (relationship using foreign key from the question class)"""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # returns choice text
    def __str__(self):
        return self.choice_text