from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('tests/', include('tests.urls', namespace='tests')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),

]
