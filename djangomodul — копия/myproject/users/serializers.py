from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from django.contrib.auth import authenticate  # Импортируем authenticate
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class LoginSerializer(serializers.Serializer):
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)  # Создаем токен обновления
            return {
                'user': user,
                'tokens': {
                    'access': str(refresh.access_token),  # Передаем токен доступа
                    'refresh': str(refresh)  # Передаем токен обновления
                }
            }
        raise serializers.ValidationError("Incorrect Credentials")
