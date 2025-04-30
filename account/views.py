from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@api_view(["POST"])
def Register(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        print(serializer)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["email"] = account.email
            data["response"] = "account has been created"

            refresh = RefreshToken.for_user(account)

            data["token"] = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def Logout(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"message": "your are logged out "})


@api_view(["POST"])
def Login(request):
    dicti = {}
    if request.method == "POST":
        data = TokenObtainPairSerializer(data=request.data)
        print(data)
        if data.is_valid():
            print("it's working")
            dicti = {
                "access": data.validated_data["access"],
                "refresh": data.validated_data["refresh"],
            }
            print(dicti["access"])

            return Response(dicti, status=status.HTTP_200_OK)
        else:
            print(data.errors)

            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)