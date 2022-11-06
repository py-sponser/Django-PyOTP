from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from rest_framework import permissions
from rest_framework.views import Response, APIView
from accounts.models import User


@method_decorator(csrf_protect, name="dispatch")
class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        if not request.user.is_authenticated:  # Only unauthenticated users can access register function.
            data = self.request.data
            full_name = data["full_name"]
            email = data["email"]
            password1 = data["password1"]
            password2 = data["password2"]
            is_doctor = data["is_doctor"]

            if full_name and email and password1 and password2:
                print(f"User is Doctor? \n> {is_doctor}")
                if password1 == password2:
                    if len(password1) < 4:
                        return Response({"password_error": "Password should be bigger than 4 characters"})
                    elif "@" not in email:
                        return Response({"email_error":"Email must contain '@', '.com .net ...'"})
                    else:
                        if User.objects.filter(email=email).exists():
                            return Response({"exist": "User already have an account."})
                        else:
                            user = User.objects.create_user(username=full_name, email=email, password=password1,
                                                            is_active=True)

                            return Response({"success": "User is created successfully."})
                else:
                    return Response({"password_error": "Password is not match."})
            else:
                return Response({"error": "Fields is empty, fill them."})
        else:
            return Response({"error": "Not allowed to register while user is already authenticated."})