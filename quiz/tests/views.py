from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Test
# Create your views here.


# class TestListView(ListView):
#     model = Test
#     template_name = 'tests/main.html'


def list_tests(request):
    tests = Test.objects.all()
    context = {
        'tests': tests
    }
    return render(request, 'tests/main.html', context)


def test_view(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    context = {
        'test': test,
        'questions': questions
    }
    return render(request, 'tests/test.html', context)
