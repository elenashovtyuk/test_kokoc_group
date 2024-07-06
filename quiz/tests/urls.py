from django.urls import path
from .views import (
    list_tests, test_view
)


urlpatterns = [
    path('', list_tests, name='list-tests'),
    path('<int:pk>/', test_view, name='test-view'),
    # path('<int:pk>/data/', test_data_view, name='test-data-view')
]
