from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import random


def index(request):
    random_q = random.choice(Question.objects.all())
    return HttpResponse(random_q)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def suggest(request):
    return HttpResponse("Suggest a question.")