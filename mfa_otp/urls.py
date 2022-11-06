from django.urls import path
from mfa_otp import views

urlpatterns = [
    path("enable/", views.EnableMFATOTP.as_view()),
    path("get-provision-uri/", views.GetProvisionURI.as_view()),
    path("verify-otp/", views.VerifyOTP.as_view()),
]