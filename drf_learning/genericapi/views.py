from django.shortcuts import render
from .models import Student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    ListModelMixin,
)
from .serializer import StudentSerializer
from .models import Student

# Create your views here.


class studentGenericAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):

    queryset = Student.objects.all()
    lookup_field = "roll"
    serializer_class = StudentSerializer

    def get(self, request):
        # return self.retrieve(request) - used when we want to retrive using roll (lookupfield)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, roll):
        return self.update(request)

    def patch(self, request, roll):
        return self.partial_update(request)

    def delete(self, request, roll):
        return self.destroy(request)
