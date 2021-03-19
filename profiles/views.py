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

        if serializer.is_valid():
            try:
                child_profile = ChildProfile.objects.get(custom_user=custom_user)
                serializer.update_profile(child_profile)
            except ChildProfile.DoesNotExist as e:
                serializer.save_profile(custom_user)
            data = serializer.data
            data['custom_user'] = custom_user.id
            return Response(data, status=status.HTTP_200_OK)

        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        if custom_user.user_type == 1:
            try:
                child_profile = ChildProfile.objects.get(custom_user=custom_user)
            except ChildProfile.DoesNotExist as e:
                return Response({}, status=status.HTTP_404_NOT_FOUND)

            serializer = ChildProfileSerializer(child_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif custom_user.user_type == 2:
            try:
                ChildProfile.objects.select_related()
                child_profiles = ChildProfile.objects.filter(
                    custom_user__email=custom_user.email,
                    custom_user__user_type=1
                )
            except ChildProfile.DoesNotExist as e:
                return Response({}, status=status.HTTP_404_NOT_FOUND)

            serializer = ChildProfileSerializer(child_profiles, many=True)
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
            try:
                parent_profile = ParentProfile.objects.get(custom_user=custom_user)
                serializer.update_profile(parent_profile)
            except ParentProfile.DoesNotExist as e:
                serializer.save_profile(custom_user)
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
            try:
                teacher_profile = TeacherProfile.objects.get(custom_user=custom_user)
                serializer.update_profile(teacher_profile)
            except TeacherProfile.DoesNotExist as e:
                serializer.save_profile(custom_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def get(self, request, *args, **kwargs):
        custom_user = CustomUser.objects.get(id=self.request.user.id)
        try:
            teacher_profile = TeacherProfile.objects.get(custom_user=custom_user)
        except TeacherProfile.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherProfileSerializer(teacher_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
