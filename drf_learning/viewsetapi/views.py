from django.shortcuts import render
from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer

# Create your views here.


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "roll"
