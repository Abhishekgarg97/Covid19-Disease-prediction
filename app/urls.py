from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


# Create your urls here.
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('password/', views.reset_password, name='password'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('archive_news/', views.archive_news, name='archive-news'),
    path('contact/', views.contact, name='contact'),
    path('donation/', views.donation, name='donation'),
    path('faq/', views.faq, name='faq'),
    path('infected/', views.infected, name='infected'),
    path('predictions/', views.predictions, name='predictions'),
    path('protection/', views.protection, name='protection'),
    path('single_news/', views.single_news, name='single_news'),
    path('slogin/', views.slogin, name='slogin'),



    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
