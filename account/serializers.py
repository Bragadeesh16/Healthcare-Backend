from rest_framework import serializers
from .models import CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "password2",
            "user_type"
        ]

    def save(self, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if not email.endswith('@gmail.com'):
            raise serializers.ValidationError({'email error': 'Enter a valid Gmail address'})


        if len(password) < 8 :
            raise serializers.ValidationError({'password1 error':'you password must minimum 8 characters'})

        if password != password2:
            raise serializers.ValidationError({"password error": "password does not match"})

        if CustomUser.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({"email error": "email id is already exists"})

        account = CustomUser(email=self.validated_data["email"], user_type=self.validated_data["user_type"])
        account.username = self.validated_data["email"].split("@")[0]
        account.set_username(account.username)
        account.set_password(password)
        account.save()

        return account
