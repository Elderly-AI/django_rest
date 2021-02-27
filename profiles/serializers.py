from rest_framework import serializers
from profiles.models import ChildProfile, ParentProfile, TeacherProfile


class ChildProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProfile
        fields = ['first_name', 'age', 'sex']

    def save(self, custom_user):
        first_name = self.validated_data['first_name']
        age = self.validated_data['age']
        sex = self.validated_data['sex']
        ChildProfile.objects.create(custom_user=custom_user, first_name=first_name, age=age, sex=sex)
        custom_user.status = 1
        custom_user.save()


class ParentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentProfile
        fields = ['first_name', 'last_name', 'patronymic', 'phone_number', 'sex']

    def save(self, custom_user):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        patronymic = self.validated_data['patronymic']
        phone_number = self.validated_data['phone_number']
        sex = self.validated_data['sex']

        ParentProfile.objects.create(custom_user=custom_user, first_name=first_name,
                                     last_name=last_name, patronymic=patronymic,
                                     phone_number=phone_number, sex=sex)
        custom_user.status = 2
        custom_user.save()


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['first_name', 'last_name', 'patronymic', 'phone_number',
                  'sex', 'about', 'specialization', 'certificates']

    def save(self, custom_user):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        patronymic = self.validated_data['patronymic']
        phone_number = self.validated_data['phone_number']
        sex = self.validated_data['sex']
        about = self.validated_data['about']
        specialization = self.validated_data['specialization']
        certificates = self.validated_data['certificates']

        TeacherProfile.objects.create(custom_user=custom_user, first_name=first_name,
                                      last_name=last_name, patronymic=patronymic,
                                      phone_number=phone_number, sex=sex, about=about,
                                      specialization=specialization, certificates=certificates)
        custom_user.status = 2
        custom_user.save()



