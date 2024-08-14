from django.contrib import admin
from .models import Question, Suggestion

admin.site.register(Question)
admin.site.register(Suggestion)