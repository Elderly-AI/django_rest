from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from user.serializers import CustomUserRegistrationSerializer, CustomUserLoginSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login
from user.models import CustomUser


class RegistrationCustomUserView(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    serializer_class = CustomUserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomUserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'email': serializer.data['email']}, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class LoginCustomUserView(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    serializer_class = CustomUserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data

        email = data.get('email', )
        password = data.get('password', )
        user = authenticate(username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

