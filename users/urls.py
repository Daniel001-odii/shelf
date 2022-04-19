from .views import profile, edit_profile
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from . import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# ...

urlpatterns = [
    # ...
    path('profile/<username>/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        subject_template_name='users/password_reset_subject.txt',
        success_url='/users/password_reset/done/'),
        name='password_reset'
    ),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url='/users/reset/done/'),
        name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path('<username>/myposts/', views.UserList.as_view(), name ="my_post"),
        ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT, document_root = settings.MEDIA_ROOT)
    