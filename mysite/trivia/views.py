from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Suggestion
from datetime import datetime
import random

# Add 404 exceptions


def index(request):
    questions = Question.objects.all()
    seen_questions = request.session.get('seen_questions', [])
    available_questions = [q for q in questions if q.id not in seen_questions]
    if not available_questions:
        seen_questions = []
        available_questions = questions
    question = random.choice(available_questions)
    seen_questions.append(question.id)
    request.session['seen_questions'] = seen_questions
    return render(request, 'trivia/index.html', {'question': question})


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