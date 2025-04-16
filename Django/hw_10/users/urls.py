from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

from . import views
from .forms import CustomLoginForm

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path(
        'login/',
        LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=CustomLoginForm
        ),
        name='login'
    ),

]
