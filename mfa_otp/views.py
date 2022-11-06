import pyotp
from rest_framework.views import Response, APIView
from rest_framework import permissions
from accounts.models import User
from mfa_otp.models import PyOTP
from mfa_otp.utils import build_uri

# Create your views here.


# don't forget to require CSRFToken
class EnableMFATOTP(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        secret_key = pyotp.random_base32()  # generates backend secret key (Give this key to google authenticator)
        user = User.objects.get(id=request.user.id)
        user.mfa = True
        user.save()
        PyOTP.objects.create(user=user, secret=secret_key, issuer_name="SPonSeR Password Manager", name=user.email)
        return Response({"success": "MFA is enabled, redirect to QR-code"})


# don't forget to require CSRFToken
class GetProvisionURI(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user_pyotp = PyOTP.objects.get(user=request.user)
        provision_uri = build_uri(secret=user_pyotp.secret, issuer=user_pyotp.issuer_name, name=user_pyotp.name,
                                  digits=user_pyotp.digits, period=user_pyotp.interval)
        return Response({"provision_uri": provision_uri})


# don't forget to require CSRFToken
class VerifyOTP(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        otp = request.data["otp"]
        if otp:
            user_pyotp = PyOTP.objects.get(user=request.user)
            totp = pyotp.TOTP(user_pyotp.secret, interval=user_pyotp.interval)
            otp_ok = totp.verify(otp)
            if otp_ok:
                return Response({"success": "OTP is valid."})
            else:
                return Response({"error": "OTP is invalid."})
        else:
            return Response({"error": "No OTP is recieved."})
