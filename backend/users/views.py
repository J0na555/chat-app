from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    },
                    "message": "User created successfully. Now log in to get tokens."
                }, status=status.HTTP_201_CREATED)

class CustomLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        print("Request data:", request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful!",
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)
        return Response({"error":"Invalid Login credentials!"}, status= status.HTTP_401_UNAUTHORIZED)
    