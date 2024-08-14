from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=100)
    published_date = models.DateTimeField('date published')
    suggested = models.BooleanField(name='suggested', default=False)

    def __str__(self):
        return self.question_text
    

class Suggestion(models.Model):
    suggestion_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=100)
    suggested_date = models.DateTimeField('date suggested')

    def __str__(self):
        return self.suggestion_text