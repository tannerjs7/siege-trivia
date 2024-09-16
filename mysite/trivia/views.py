from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Suggestion
from datetime import datetime
import random

# Add 404 exceptions

def index(request):
    # random_q = random.choice(Question.objects.all())
    random_q = list(Question.objects.all())
    random.shuffle(random_q)
    context = {'random_q': random_q}
    return render(request, 'trivia/index.html', context)


def detail(request):
    all_suggestions = list(Suggestion.objects.all())
    context = {'all_suggestions': all_suggestions}
    return render(request, 'trivia/detail.html', context)


def suggest(request):
    try:
        suggestion = Suggestion(
            suggestion_text=request.POST['question'],
            answer_text=request.POST['answer'],
            suggested_date=datetime.now()
        )
    except (KeyError, Suggestion.DoesNotExist):
        return render(request, 'trivia/detail.html', {
            'error_message': 'Try again.'
        })
    else:
        suggestion.save()
        return HttpResponseRedirect(reverse('trivia:detail'))