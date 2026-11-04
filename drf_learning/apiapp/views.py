from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from .models import Profile
from rest_framework.views import APIView

# Create your views here.


@api_view(["GET", "POST", "PATCH"])
def home(request):
    if request.method == "POST":
        print(request.GET.get("status"))
        print(request.data.get("name"))

        return Response(
            {"status": 200, "message": "POST request received", "method": "P    OST"}
        )
    elif request.method == "GET":
        return Response({"status": 200, "message": "Its working!!", "method": "Get"})
    elif request.method == "PATCH":
        return Response({"status": 200, "message": "Its working!!", "method": "Patch"})
    else:
        return Response(
            {"status": 400, "message": "Invalid method called", "method": "Invalid"}
        )


@api_view(["GET"])
def get_profile(request):

    data = Profile.objects.all()
    serializer = UserSerializer(data, many=True)

    return Response({"message": "Success", "data": serializer.data})


@api_view(["POST"])
def post_profile(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {"message": "User created Successfully", "data": serializer.data},
            status=201,
        )

    return Response(
        {"message": "Something went wrong", "errors": serializer.errors}, status=400
    )


@api_view(["PUT"])
def put_profile(request, uname):

    try:

        profile = Profile.objects.get(username=uname)

        serializer = UserSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Updated sucessfully", "data": serializer.data}, status=200
            )

        return Response(
            {
                "message": "Invalid data",
                "errors": serializer.error_messages,
            }
        )

    except Profile.DoesNotExist:
        return Response({"message": "User not found", "Username": uname})


@api_view(["PATCH"])
def patch_profile(request, uname):

    try:

        profile = Profile.objects.get(username=uname)

        serializer = UserSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Updated sucessfully", "data": serializer.data}, status=200
            )

        return Response(
            {
                "message": "Invalid data",
                "errors": serializer.error_messages,
            }
        )

    except Profile.DoesNotExist:
        return Response({"message": "User not found", "Username": uname})


@api_view(["DELETE"])
def delete_profile(request, uname):

    try:
        profile = Profile.objects.get(username=uname)
    except Profile.DoesNotExist:
        return Response({"message": "User not found", "Username": uname})

    password = request.data.get("password")

    if not password:
        return Response({"message": "Password required"})

    if profile.check_password(password):
        profile.delete()
        return Response({"message": "user deleted"})

    return Response({"message": "Invalid Password"})


class ProfileAPIView(APIView):
    def get(self, request):
        return Response({"msg": "APIView working"})

    def post(self, request):
        pass

    def patch(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
