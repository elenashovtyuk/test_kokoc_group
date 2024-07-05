from django.urls import path
from .views import (
    TestListView, test_view
)


urlpatterns = [
    path('', TestListView.as_view(), name='main-view'),
    path('<pk>/', test_view, name='test-view')
]
