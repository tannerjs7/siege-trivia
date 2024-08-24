from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
import random


def index(request):
    random_q = random.choice(Question.objects.all())
    context = {'random_q': random_q}
    return render(request, 'trivia/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def suggest(request):
    return HttpResponse("Suggest a question.")