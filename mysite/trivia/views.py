from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question
from datetime import datetime
import random

# Add 404 exceptions


def index(request):
    questions = Question.objects.filter(suggested=False)
    seen_questions = request.session.get('seen_questions', [])
    available_questions = [q for q in questions if q.id not in seen_questions]
    if not available_questions:
        seen_questions = []
        available_questions = questions
    question = random.choice(available_questions)
    seen_questions.append(question.id)
    request.session['seen_questions'] = seen_questions
    return render(request, 'trivia/index.html', {'question': question})


def suggestions(request):
    all_suggestions = list(Question.objects.filter(suggested=True))
    context = {'all_suggestions': all_suggestions}
    return render(request, 'trivia/suggestions.html', context)


def suggest(request):
    try:
        suggestion = Question(
            question_text=request.POST['question'],
            answer_text=request.POST['answer'],
            created_date=datetime.now(),
            suggested=True
        )
    except (KeyError, Question.DoesNotExist):
        return render(request, 'trivia/suggestions.html', {
            'error_message': 'Try again.'
        })
    else:
        suggestion.save()
        return HttpResponseRedirect(reverse('trivia:suggestions'))