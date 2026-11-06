from django.contrib.auth import get_user_model, authenticate

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authtoken.models import Token

from .models import Student
from .serializers import StudentSerializer

User = get_user_model()


# REGISTER
class RegisterView(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(**{User.USERNAME_FIELD: username}).exists():

            return Response(
                {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            **{User.USERNAME_FIELD: username, "password": password}
        )

        return Response(
            {"message": "Registered successfully"}, status=status.HTTP_201_CREATED
        )


# LOGIN
class LoginView(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):

        identifier = request.data.get(User.USERNAME_FIELD)
        password = request.data.get("password")

        if not identifier or not password:
            return Response(
                {"error": "Credentials required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(
            request, **{User.USERNAME_FIELD: identifier, "password": password}
        )

        if user is None:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "Login successful", "token": token.key})


# LOGOUT
class LogoutView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        request.auth.delete()

        return Response({"message": "Logout successful"})


# STUDENT CRUD
class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = "username"
