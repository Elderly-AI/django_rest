from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from user.models import CustomUser
from profiles.models import ChildProfile, ParentProfile, TeacherProfile
from profiles.serializers import ChildProfileSerializer, ParentProfileSerializer, TeacherProfileSerializer


class ChildProfileView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ChildProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ChildProfileSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            custom_user = CustomUser.objects.get(id=self.request.user.id)
            serializer.save(custom_user)
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        child_profile = ChildProfile.objects.get(custom_user=custom_user)
        serializer = ChildProfileSerializer(child_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParentProfileView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ChildProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ChildProfileSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            custom_user = CustomUser.objects.get(id=self.request.user.id)
            serializer.save(custom_user)
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        parent_profile = ParentProfile.objects.get(custom_user=custom_user)
        serializer = ParentProfileSerializer(parent_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherProfileView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ChildProfileSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ChildProfileSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            custom_user = CustomUser.objects.get(id=self.request.user.id)
            serializer.save(custom_user)
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        teacher_profile = TeacherProfile.objects.get(custom_user=custom_user)
        serializer = TeacherProfileSerializer(teacher_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
