from django.urls import path
from .views import RegisterView,OTPVerifyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-otp/', OTPVerifyView.as_view(), name='verify-otp'),
]
