from django.db import models


class Test(models.Model):
    """Модель теста, квиза."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    count_of_questions = models.IntegerField

    def __str__(self):
        return self.name
