from django.db import models


# Create your models here.
class Test(models.Model):
    """Модель теста, квиза."""
    name = models.CharField(max_length=120)
    count_of_questions = models.IntegerField

    def __str__(self):
        return self.name
