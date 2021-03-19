from rest_framework import serializers
from profiles.models import ChildProfile, ParentProfile, TeacherProfile


class ChildProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProfile
        fields = ['first_name', 'age', 'sex', 'custom_user']
        extra_kwargs = {'custom_user': {'required': False, 'allow_null': True}}

    def update_profile(self, profile):
        profile.first_name = self.validated_data['first_name']
        profile.age = self.validated_data['age']
        profile.sex = self.validated_data['sex']
        profile.save()

    def save_profile(self, custom_user):
        return ChildProfile.objects.create(
            custom_user=custom_user,
            first_name=self.validated_data['first_name'],
            age=self.validated_data['age'],
            sex=self.validated_data['sex']
        )


class ParentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentProfile
        fields = ['first_name', 'last_name', 'patronymic', 'phone_number', 'sex']

    def validate_user_type(self, custom_user):
        if custom_user.user_type != 2:
            raise serializers.ValidationError('You are not parent')

    def update_profile(self, profile):
        profile.first_name = self.validated_data['first_name']
        profile.last_name = self.validated_data['last_name']
        profile.patronymic = self.validated_data['patronymic']
        profile.phone_number = self.validated_data['phone_number']
        profile.sex = self.validated_data['sex']
        profile.save()

    def save_profile(self, custom_user):
        return ParentProfile.objects.create(
            custom_user=custom_user,
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            patronymic=self.validated_data['patronymic'],
            phone_number=self.validated_data['phone_number'],
            sex=self.validated_data['sex']
        )


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['first_name', 'last_name', 'patronymic', 'phone_number',
                  'sex', 'about', 'specialization']

    def validate_user_type(self, custom_user):
        if custom_user.user_type != 3:
            raise serializers.ValidationError('You are not teacher')

    def update_profile(self, profile):
        profile.first_name = self.validated_data['first_name']
        profile.last_name = self.validated_data['last_name']
        profile.patronymic = self.validated_data['patronymic']
        profile.phone_number = self.validated_data['phone_number']
        profile.sex = self.validated_data['sex']
        profile.about = self.validated_data['about']
        profile.specialization = self.validated_data['specialization']
        profile.save()

    def save_profile(self, custom_user):
        return TeacherProfile.objects.create(
            custom_user=custom_user,
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            patronymic=self.validated_data['patronymic'],
            phone_number=self.validated_data['phone_number'],
            sex=self.validated_data['sex'],
            about=self.validated_data['about'],
            specialization=self.validated_data['specialization'],
        )




