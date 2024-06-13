from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenRefreshView

class TokenRefreshView(TokenRefreshView):
    pass
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        return Response({
            'success': True,
            'message': 'Success',
            'token': str(token.access_token)
        }, status=status.HTTP_200_OK)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = RefreshToken.for_user(user)
        return Response({
            'success': True,
            'message': 'Success',
            'token': str(token.access_token)
        }, status=status.HTTP_200_OK)
