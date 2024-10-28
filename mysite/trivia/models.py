from django.db import models
from datetime import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', default=datetime.now())
    suggested = models.BooleanField(name='suggested', default=False)

    def __str__(self):
        return self.question_text