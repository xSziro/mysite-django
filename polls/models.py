from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_lenght = 400)
    publication_date = models.DateTimeField('date of publishing')

class choice(models.Model):
    question = models.ForeingKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_lenght=200)
    votes = models.IntegerFields(default=0)
