from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User

from .models import Student
from .serializer import StudentSerializer

# Create your views here.


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "username"

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["post"]

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password)
        return Response(
            {"message": "User registered successfully", "username": user.username},
            status=status.HTTP_201_CREATED,
        )
