from django.shortcuts import render
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializer import StudentSerializer

# Create your views here.


@ensure_csrf_cookie
def csrf_token_view(request):
    return JsonResponse({"csrfToken": get_token(request)})


User = get_user_model()


@method_decorator(csrf_protect, name="dispatch")
class LoginView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        identifier = request.data.get(User.USERNAME_FIELD)
        password = request.data.get("password")
        if not identifier or not password:
            return Response(
                {"error": "Credentials are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        credentials = {User.USERNAME_FIELD: identifier, "password": password}

        user = authenticate(request, **credentials)

        if user is None:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {"error": "Account is inactive"}, status=status.HTTP_403_FORBIDDEN
            )

        login(request, user)
        return Response(
            {"message": "Login successful", "user": getattr(user, User.USERNAME_FIELD)},
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "username"

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
