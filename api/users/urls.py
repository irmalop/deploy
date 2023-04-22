from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, ResendVerifyEmail, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView, ChangePasswordView
urlpatterns=[
    path('signup/', RegisterView.as_view(), name = "register"),
    path('login/', LoginAPIView.as_view(), name = "login"), 
    path('email/verify/', VerifyEmail.as_view(), name = "email-verify"),
    path('resend/email/verify/', ResendVerifyEmail.as_view(), name = "resend email verify"),
    path('request/reset/email/', RequestPasswordResetEmail.as_view(), name = "request-reset-email/"),
    path('password/reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name = "password-reset-confirm"),
    path('password/reset/complete/', SetNewPasswordAPIView.as_view(), name = "password-reset/complete"),
    path('change/password/', ChangePasswordView.as_view(), name='change-password'),


]