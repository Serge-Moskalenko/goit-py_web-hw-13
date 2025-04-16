from django.contrib import admin
from django.urls import path, include,reverse_lazy
from django.contrib.auth import views as auth_views

from users.forms import CustomPasswordResetForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path("users/", include("users.urls")),
    path('password_reset/', auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset_form.html',
    email_template_name='registration/password_reset_email.html',
    subject_template_name='registration/password_reset_subject.txt',
    form_class=CustomPasswordResetForm
), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
