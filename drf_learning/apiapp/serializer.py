from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        extra_kwargs = { # write only just accepts password from api dont send back to api when get is called
            'password': {'write_only': True}
        }

    def create(self, validated_data): # for hashing password as only serializer.save() in views.py does not hash the password
        return Profile.objects.create_user(**validated_data)

    
    def validate_age(self, value): # if value is correct it must return same value
        if value<18:
            raise serializers.ValidationError("Age must be more than 18")

        return value

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Email must be google account")

        return value
    