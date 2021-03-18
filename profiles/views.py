from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from profiles.serializers import ChildProfileSerializer, ParentProfileSerializer, TeacherProfileSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from user.models import CustomUser
from profiles.models import ChildProfile, ParentProfile, TeacherProfile


class ChildProfileView(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    serializer_class = ChildProfileSerializer
    queryset = ChildProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChildProfileSerializer(data=request.data)
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        serializer.validate_user_type(custom_user)

        if serializer.is_valid():
            serializer.save(custom_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        try:
            child_profile = ChildProfile.objects.get(custom_user=custom_user)
        except ChildProfile.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChildProfileSerializer(child_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParentProfileView(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    serializer_class = ParentProfileSerializer
    queryset = ParentProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ParentProfileSerializer(data=request.data)
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        serializer.validate_user_type(custom_user)

        if serializer.is_valid():
            serializer.save(custom_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        try:
            parent_profile = ParentProfile.objects.get(custom_user=custom_user)
        except ParentProfile.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ParentProfileSerializer(parent_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherProfileView(CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    serializer_class = TeacherProfileSerializer
    queryset = TeacherProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = TeacherProfileSerializer(data=request.data)
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        serializer.validate_user_type(custom_user)

        if serializer.is_valid():
            serializer.save(custom_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        try:
            teacher_profile = TeacherProfile.objects.get(custom_user=custom_user)
        except ParentProfile.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherProfileSerializer(teacher_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
