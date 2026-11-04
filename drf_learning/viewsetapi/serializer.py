from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_age(self, value):  # if value is correct it must return same value
        if value < 18:
            raise serializers.ValidationError("Age must be more than 18")

        return value

    def validate_email(self, value):
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Email must be google account")
        return value
