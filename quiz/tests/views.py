from django.shortcuts import render, get_object_or_404
from .models import Test


def list_tests(request):
    tests = Test.objects.all()
    context = {
        'tests': tests
    }
    return render(request, 'tests/main.html', context)


def test_view(request, pk):
    test = get_object_or_404(Test, id=pk)
    questions = test.questions.all()
    answers = []
    for question in questions:

        for answer in question.answers.all():
            answers.append(answer)

    context = {
        'test': test,
        'questions': questions,
        'answers': answers
    }
    return render(request, 'tests/test.html', context)
