from django.shortcuts import render
from django.views.generic import ListView
from .models import Test
# Create your views here.


class TestListView(ListView):
    model = Test
    template_name = 'tests/main.html'


def test_view(request, pk):
    test = Test.objects.get(pk=pk)
    return render(request, 'tests/test.html', {'obj': test})
