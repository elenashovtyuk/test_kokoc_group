from django.urls import path
from .views import (
    list_tests, test_view
)

app_name = 'tests'

urlpatterns = [

    path('', list_tests, name='list-tests'),
    path('<int:pk>/', test_view, name='test-view'),
]
