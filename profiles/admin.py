from django.contrib import admin
from profiles.models import ChildProfile, ParentProfile, TeacherProfile


admin.site.register(ChildProfile)
admin.site.register(ParentProfile)
admin.site.register(TeacherProfile)
