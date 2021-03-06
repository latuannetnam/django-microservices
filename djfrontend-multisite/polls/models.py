from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    class APIMeta:
        db_name = 'site1.test.com'


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name='choices', db_column='question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class APIMeta:
        db_name = 'site1.test.com'
