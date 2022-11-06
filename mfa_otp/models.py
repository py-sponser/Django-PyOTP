from django.db import models
from accounts.models import User


class PyOTP(models.Model):
    """pyotp model

        Here we will store secret of every generated otp. So that on verification of OTP we know which secret to use
    """

    # Attributes
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    secret = models.CharField(max_length=50, null=False, blank=False)
    interval = models.IntegerField(default=30, null=True, blank=True)
    digits = models.IntegerField(default=6, null=True, blank=True)
    issuer_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        # Application Name to show in Google Authenticator
    )
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        # (Username or Email Address) that is shown beside application name in Google Authenticator
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
