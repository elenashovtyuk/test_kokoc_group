from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from users.views import SignUp

app_name = 'users'

urlpatterns = [
    path(
        'auth/login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'auth/logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    )
]
