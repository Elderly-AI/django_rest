"""speech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import RegistrationCustomUserView, LoginCustomUserView
from profiles.views import ChildProfileView, ParentProfileView, TeacherProfileView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/reg', RegistrationCustomUserView.as_view(), name='reg'),
    path('api/v1/login', LoginCustomUserView.as_view(), name='login'),

    path('api/v1/profile/child', ChildProfileView.as_view(), name='child_profile'),
    path('api/v1/profile/parent', ParentProfileView.as_view(), name='parent_profile'),
    path('api/v1/profile/teacher', TeacherProfileView.as_view(), name='teacher_profile'),
]
