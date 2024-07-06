from django.db import models
from tests.models import Test


class Question(models.Model):
    """Модель вопроса квиза."""
    text_of_question = models.CharField(max_length=120)
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    def __str__(self):
        return str(self.text_of_question)

    # def get_answer(self):
    #     return self.answer_set.all()


class Answer(models.Model):
    """Модель ответа на вопрос."""
    text_of_answer = models.CharField(max_length=120)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    def __str__(self):
        return f'question: {self.question}, answer: {self.text_of_answer}'
