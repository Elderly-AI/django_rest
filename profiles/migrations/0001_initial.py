# Generated by Django 3.1.7 on 2021-02-27 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=32)),
                ('last_name', models.CharField(default='', max_length=32)),
                ('patronymic', models.CharField(default='', max_length=32)),
                ('phone_number', models.CharField(default='', max_length=32)),
                ('sex', models.BooleanField(default=False)),
                ('about', models.CharField(default='', max_length=1024)),
                ('specialization', models.CharField(default='', max_length=32)),
                ('custom_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=32)),
                ('last_name', models.CharField(default='', max_length=32)),
                ('patronymic', models.CharField(default='', max_length=32)),
                ('phone_number', models.CharField(default='', max_length=32)),
                ('sex', models.BooleanField(default=False)),
                ('custom_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChildProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=32)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('sex', models.BooleanField(default=False)),
                ('custom_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
