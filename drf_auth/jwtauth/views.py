from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
